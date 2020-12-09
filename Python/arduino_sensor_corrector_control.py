# arduino_sensor_corrector_control.py
import mysql.connector
# Database connection

import datetime
# Gets curent datetime

import sql_queeries_and_insertions as sql
# file of often used sql queeries and insertion code


def turn_all_correctors_off(region_id, cnx, ser):
   cursor = cnx.cursor()
   querry_get_corrector_info = ("""
       SELECT
           IC.CorrectorID,
           IC.CorrectorPin
       FROM
           InstalledCorrectors IC
       WHERE
           IC.FarmRegion_RegionID = '%(RegionID)s'
       """)
   data_region_id = {
       'RegionID': region_id
   }
   cursor.execute(querry_get_corrector_info, data_region_id)
   for (CorrectorID, CorrectorPin) in cursor:
       if CorrectorPin is None:
           # LED corrector
           cnx_2 = mysql.connector.connect(**sql.config)
           cursor_2 = cnx_2.cursor()
           querry_get_all_led_pins = ("""
               SELECT
                   RedPin,
                   GreenPin,
                   BluePin
               FROM
                   LEDCorrector
               WHERE
                   InstalledCorrectors_CorrectorID = '%(CorrectorID)s'
               """)
           data_get_all_led_pins = {
               'CorrectorID': CorrectorID
           }
           cursor_2.execute(querry_get_all_led_pins, data_get_all_led_pins)
           for (RedPin, GreenPin, BluePin) in cursor_2:
               ser.write("c002{:03}0".format(RedPin))
               correction_response = ser.readline()
               while correction_response != 'Correction Made\r\n':
                   correction_response = ser.readline()
               ser.write("c002{:03}0".format(GreenPin))
               correction_response = ser.readline()
               while correction_response != 'Correction Made\r\n':
                   correction_response = ser.readline()
               ser.write("c002{:03}0".format(BluePin))
               correction_response = ser.readline()
               while correction_response != 'Correction Made\r\n':
                   correction_response = ser.readline()
           cursor_2.close()
           cnx_2.close()
       else:  # Other corrector
           ser.write("c002{:03}0".format(CorrectorPin))
           correction_response = ser.readline()
           while correction_response != 'Correction Made\r\n':
               correction_response = ser.readline()
       # Save change to db
       if bool(sql.check_if_corrector_is_on(CorrectorID, cnx)):
           sql.turn_correction_off(datetime.datetime.now(), int(CorrectorID), cnx)


def get_all_sensor_data_in_region(region_id, cnx, ser):
   cursor = cnx.cursor()
   querry_get_all_sensor_data_in_region = (
       """
       SELECT
           I_S.SensorID,
           I_S.SensorTypes_SensorTypeID,
           I_S.Internal,
           I_S.SensorInputPin,
           I_S.sensorPowerPin,
           PR.RelayPin,
           I2C.AddrFloatOrGround
       FROM
           InstalledSensors I_S
               LEFT JOIN
           PowerRelay PR ON I_S.SensorID = PR.InstalledSensors_SensorID
               LEFT JOIN
           I2cBusSensor I2C ON I_S.SensorID = I2C.InstalledSensors_SensorID
       WHERE
           I_S.FarmRegion_RegionID = 1
       """)
   data_get_all_sensor_data_in_region = {
       'RegionID': region_id
   }

   cursor.execute(querry_get_all_sensor_data_in_region, data_get_all_sensor_data_in_region)

   for (SensorID, SensorTypes_SensorTypeID, Internal, SensorInputPin, sensor_power_pin, RelayPin,
        AddrFloatOrGround) in cursor:
       # Convert None (no power pin) to 255 (Arduino will ignore 255)
       if sensor_power_pin is None:
           sensor_power_pin = 255

       # PH Sensor
       if SensorTypes_SensorTypeID == 1:
           ser.write('s{:03}{:03}{:03}'.format(SensorTypes_SensorTypeID, SensorInputPin, sensor_power_pin))
           print('s{:03}{:03}{:03}'.format(SensorTypes_SensorTypeID, SensorInputPin, sensor_power_pin))

           raw_ph_reading = ser.readline()
           ph_value = 17.5 * (int(raw_ph_reading) / 1024)
           print(ph_value)
           sql.add_sensor_data(datetime.datetime.now(), SensorID, ph_value, cnx)

       # Water Level
       elif SensorTypes_SensorTypeID == 2:
           print("s{:03}{:03}{:03}{:03}".format(SensorTypes_SensorTypeID, SensorInputPin, sensor_power_pin, RelayPin))
           ser.write(
               "s{:03}{:03}{:03}{:03}".format(SensorTypes_SensorTypeID, SensorInputPin, sensor_power_pin, RelayPin))
           print("sent to arduino")
           try:
               raw_water_height_data = ser.readline()
           except:
               print("exception reached")
               raw_water_height_data = 0
           print("Water level read")
           if int(raw_water_height_data) <= 340:
               # if input lower than 340 equation creates below 0.1 and negatives.
               water_volume = 0
           else:
               # 1296 = container base area or ml per mm height
               # water_volume = int(((int(raw_water_height_data) * 0.356) - 97.319) * 1296)
               water_volume = int((((9 * pow(10, -25)) * pow((int(raw_water_height_data)), 9.1084)) * 0.1) * 1296)
           print(int(water_volume))
           sql.add_sensor_data(datetime.datetime.now(), SensorID, water_volume, cnx)

       # Lux
       elif SensorTypes_SensorTypeID == 3:
           print("s{:03}{:03}{:1}".format(SensorTypes_SensorTypeID, SensorID, AddrFloatOrGround))
           ser.write("s{:03}{:03}{:1}".format(SensorTypes_SensorTypeID, SensorID, AddrFloatOrGround))
           print("waiting for lux reading")
           lux_reading = ser.readline()
           print(int(lux_reading))
           sql.add_sensor_data(datetime.datetime.now(), SensorID, lux_reading, cnx)

       # DHT22 sensor
       # type = 4 for temperature and type = 5 for humidity
       elif SensorTypes_SensorTypeID == 4 or SensorTypes_SensorTypeID == 5:
           print("s{:03}{:03}{:03}".format(SensorTypes_SensorTypeID, SensorInputPin, sensor_power_pin))
           ser.write("s004{:03}{:03}".format(SensorInputPin, sensor_power_pin))
           sensor_read = ser.readline()
           print(float(int(sensor_read) / 10))
           sql.add_sensor_data(datetime.datetime.now(), SensorID, float(int(sensor_read) / 10), cnx)

   cursor.close()


def carry_out_corrections_on_all_modules(region_id, cnx, ser):
   cursor = cnx.cursor()
   querry_get_module_conditions_info = ("""
       SELECT
           CM.ModuleID,
           CM.ModuleCode,
           DC.UpperLimit,
           DC.LowerLimit
       FROM
           CorrectionModule CM
               INNER JOIN
           DesiredConditions DC ON CM.ModuleID = DC.CorrectionModule_ModuleID
       WHERE
           CM.FarmRegion_RegionID = '%(RegionID)s'
               AND
           (
           DC.ConditionEndTime IS NULL
               OR
           DC.ConditionEndTime >= NOW()
           )
           AND DC.ConditionStartTime <= NOW()       
   """)
   data_get_module_conditions_info = {
       'RegionID': region_id
   }
   cursor.execute(querry_get_module_conditions_info, data_get_module_conditions_info)
   for (ModuleID, ModuleCode, UpperLimit, LowerLimit) in cursor:
       print("Condition upper limit: " + str(UpperLimit) + " condition lower limit: " + str(LowerLimit))
       # get sensorID for sensor
       sensor_id = sql.get_sensor_id_with_module_info(ModuleID, ModuleCode, cnx)
       print ("Sensor ID: " + str(sensor_id[0]))
       # get sensor reading
       sensor_reading = sql.get_most_recent_sensor_reading(int(sensor_id[0]), cnx)
       print ("Most recent sensor reading with sensor id " + str(sensor_id[0]) + ": " + str(sensor_reading[0]))
       if ModuleCode == 1:
           # PH Module
           # compare sensor reading to limits
           if float(sensor_reading[0]) > float(UpperLimit):
               # Water more basic than desired
               print ("Corrrection required, ph>upper limit")
               # get sensorID for water level using Water volume sensor type id = 2
               water_sensor_id = sql.get_sensor_id_with_module_info(ModuleID, 2, cnx)
               # get water volume sensor reading
               water_volume = sql.get_most_recent_sensor_reading(water_sensor_id[0], cnx)
               print ("Most recent water level with sensor id " + water_sensor_id + ": " + str(water_volume[0]))
               # calculate ph required
               desired_ph_decrease = float(sensor_reading[0]) - (
                       (float(LowerLimit)) + (float(UpperLimit) - float(LowerLimit)) / 2)
               equaliser_required = float((water_volume[0] * desired_ph_decrease) * 0.01)
               print("For a ph decrease of " + str(desired_ph_decrease) + ", " + str(
                   equaliser_required) + " ml of equaliser is needed")
               # get ph corrector info using PH correctoion type 1
               corrector_info = sql.get_corrector_info(ModuleID, 1, cnx)
               print("valve corrector pin is: " + str(corrector_info[0]))
               # send corrector info to arduino, flow rate is 2ml/s and x1000 as Arduino delay in ms
               ser.write("c001{:03}{:05}".format(int(corrector_info[0]), int(
                   equaliser_required * 2000)))
               corrcetion_response = ser.readline()
               while corrcetion_response != 'Correction Made\r\n':
                   corrcetion_response = ser.readline()
               start_time = datetime.datetime.now() - datetime.timedelta(seconds=equaliser_required * 2)
               sql.turn_correction_on(start_time, corrector_info[1], cnx)
               sql.add_ph_correction_data(start_time, corrector_info[1], equaliser_required, cnx)
               sql.turn_correction_off(datetime.datetime.now(), int(corrector_info[1]), cnx)

       # WaterSensorModule
       elif ModuleCode == 2:
           # Get correcor pump pin water pump has corrector type 2
           corrector_info = sql.get_corrector_info(ModuleID, 2, cnx)
           # Get if pump is on or off
           pump_on = bool(sql.check_if_corrector_is_on(corrector_info[0], cnx))
           print("pump on is " + str(pump_on))
           if float(sensor_reading[0]) < float(LowerLimit) and pump_on:
               # Turn pump off
               print("Turning off pump")
               ser.write("c002{:03}0".format(int(corrector_info[0])))
               corrcetion_response = ser.readline()
               while corrcetion_response != 'Correction Made\r\n':
                   corrcetion_response = ser.readline()
               # Save change to db
               sql.turn_correction_off(datetime.datetime.now(), int(corrector_info[1]), cnx)
           if float(sensor_reading[0]) > float(LowerLimit) and not pump_on:
               print("Turning on pump")
               # Turn pump on
               ser.write("c002{:03}1".format(int(corrector_info[0])))
               print("c002{:03}1".format(int(corrector_info[0])))
               corrcetion_response = ser.readline()
               while corrcetion_response != 'Correction Made\r\n':
                   corrcetion_response = ser.readline()
               # Save change to db
               sql.turn_correction_on(datetime.datetime.now(), corrector_info[1], cnx)
       elif ModuleCode == 4 or ModuleCode == 5:
           # temp module & humid module
           print("Temp module, upper temp level: " + str(UpperLimit))
           # get sensorID for internal dht22 sensor
           sensor_id = sql.get_int_sensor_id_with_module_and_sensor_type(ModuleID, ModuleCode, True, cnx)
           print ("Sensor ID: " + str(sensor_id[0]))
           # get sensor reading
           int_temp = sql.get_most_recent_sensor_reading(int(sensor_id[0]), cnx)
           print ("Most recent temp/humidity reading: " + str(int_temp[0]))
           # Get correcor pin for fan
           corrector_info = sql.get_corrector_info(ModuleID, ModuleCode, cnx)
           # Get if fan is on or off

           fan_on = bool(sql.check_if_corrector_is_on(corrector_info[1], cnx))
           print("Fan on: " + str(fan_on))
           if (float(int_temp[0]) < float(UpperLimit)) and fan_on == 1:
               # Turn pump off
               print("turning off fan")
               ser.write("c002{:03}0".format(int(corrector_info[0])))
               print("c002{:03}0".format(int(corrector_info[0])))
               corrcetion_response = ser.readline()
               while corrcetion_response != 'Correction Made\r\n':
                   corrcetion_response = ser.readline()
               # Save change to db
               sql.turn_correction_off(datetime.datetime.now(), int(corrector_info[1]), cnx)
           if (float(int_temp[0]) > float(UpperLimit)) and fan_on == 0:
               print("Turning on fan")
               # Turn fan on
               ser.write("c002{:03}1".format(int(corrector_info[0])))
               print("c002{:03}1".format(int(corrector_info[0])))
               corrcetion_response = ser.readline()
               print(corrcetion_response)
               while corrcetion_response != 'Correction Made\r\n':
                   corrcetion_response = ser.readline()
               print("fan correction made")
               # Save change to db
               # Fan has corrcetion id 4
               sql.turn_correction_on(datetime.datetime.now(), corrector_info[1], cnx)

       elif ModuleCode == 3:
           # Light module
           print("Light")
           # update sensor id with external id, light senor type id = 3
           ext_sensor_id = sql.get_int_sensor_id_with_module_and_sensor_type(ModuleID, 3, False, cnx)
           # check if the sensor ID alreayd attained is the same as the external
           if ext_sensor_id != sensor_id:
               ext_sensor_reading = sql.get_most_recent_sensor_reading(sensor_id[0], cnx)
           else:
               ext_sensor_reading = sensor_reading

           # LED strip has corrector ID 3
           corrector_info = sql.get_corrector_info(ModuleID, 3, cnx)
           leds_on = bool(sql.check_if_corrector_is_on(corrector_info[1], cnx))
           if ext_sensor_reading[0] > float(LowerLimit) and leds_on == 1:
               # Light enough without light so turn them off
               print("Light doesn't need to be on")
               # if leds_on:
               print("Light was on and is about to turn off")
               pins_array = sql.get_led_pins(int(corrector_info[1]), cnx)
               for i in range(0, 3):
                   ser.write("c002{:03}0".format(int(pins_array[i])))
                   print("c002{:03}0".format(int(pins_array[i])))
                   corrcetion_response = ser.readline()
                   while corrcetion_response != 'Correction Made\r\n':
                       corrcetion_response = ser.readline()
               sql.turn_correction_off(datetime.datetime.now(), int(corrector_info[1]), cnx)

           if ext_sensor_reading[0] < float(LowerLimit) and leds_on == 0:
               print("Light should be on")
               intensity = 255
               print("Light was off and about to turn on")
               rgb_array = sql.get_desired_rgb_percentages(ModuleID, cnx)
               pins_array = sql.get_led_pins(int(corrector_info[1]), cnx)
               print("red pin: " + str(pins_array[0]) + " green pin: " + str(pins_array[1]) + " blue pin: " + str(
                   pins_array[2]))
               print("red percent: " + str(rgb_array[0]) + "green percent: " + str(
                   rgb_array[1]) + "blue percent: " + str(rgb_array[2]))
               for i in range(0, 3):
                   colour_output = int(intensity * (float(rgb_array[i]) / 100))
                   ser.write("c003{:03}{:05}1".format(int(pins_array[i]), colour_output))
                   print("c003{:03}{:05}1".format(int(pins_array[i]), colour_output));
                   corrcetion_response = ser.readline()
                   while corrcetion_response != 'Correction Made\r\n':
                       corrcetion_response = ser.readline()
               sql.turn_correction_on(datetime.datetime.now(), corrector_info[1], cnx)
   cursor.close()

