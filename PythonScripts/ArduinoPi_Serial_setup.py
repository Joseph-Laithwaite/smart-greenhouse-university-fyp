#import serial
import mysql.connector
import datetime
from mysql.connector import errorcode

config={
    'user':'joseph',
    'password':'passcode',
    'host':'localhost',
    'database':'SmartGreenhouse',
    'raise_on_warnings':True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

#ser=serial.Serial("/dev/ttyUSB0",9600)
#ser.baudrate=9600
#read_ser=ser.readline()

def add_sensor_data(time, sensor_id, sensor_reading):
	add_sensor_reading = ("INSERT INTO SmartGreenhouse.SensorReadings"
                      "(TimeStamp, InstalledSensors_SensorID, SensorValue)"
                      "VALUES(%(TimeStamp)s, %(InstalledSensors_SensorID)s, %(SensorValue)s);"
                      )
	data_sensor_reading = {
 		'TimeStamp':time, 
  		'InstalledSensors_SensorID':sensor_id, 
  		'SensorValue':sensor_reading,
		}

	cursor.execute(add_sensor_reading, data_sensor_reading)
	cnx.commit()
	cursor.close()
	cnx.close()

def add_start_correction_action_data(start_time, corrector_id):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_start_correction_action = ("INSERT INTO SmartGreenhouse.CorrectionAction"
                        "(TimeStampStart, InstalledCorrectors_CorrectorID)"						#, TimeStampEnd)"
                        "VALUES(%(TimeStampStart)s, %(InstalledCorrectors_CorrectorID)s);"		#, %(TimeStampEnd)s);"
                        )

	data_start_correction_action = {
	  'TimeStampStart':start_time, 
	  'InstalledCorrectors_CorrectorID':corrector_id, 
	  #'TimeStampEnd':,
	}

	cursor.execute(add_start_correction_action, data_start_correction_action)
	cnx.commit()
	cursor.close()
	cnx.close()

def add_ph_correction_data(start_time, corrector_id, ph_equaliser_volume):
	add_start_correction_action_data(start_time, corrector_id)
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_ph_correction = ("INSERT INTO SmartGreenhouse.PHCorrection"
    	                "(PHEqualiserVolume, CorrectionAction_TimeStampStart, CorrectionAction_InstalledCorrectors_CorrectorID)"
        	            "VALUES(%(PHEqualiserVolume)s, %(CorrectionAction_TimeStampStart)s, %(CorrectionAction_InstalledCorrectors_CorrectorID)s);"
            	        )
	data_ph_correction = {
	   'PHEqualiserVolume':ph_equaliser_volume, 
	   'CorrectionAction_TimeStampStart':start_time, 
	   'CorrectionAction_InstalledCorrectors_CorrectorID':corrector_id,
	   }

	cursor.execute(add_ph_correction, data_ph_correction)
	cnx.commit()
	cursor.close()
	cnx.close()


def add_led_correction_data(start_time, corrector_id, red_value, green_value, blue_value, intensity):
	add_start_correction_action_data(start_time, corrector_id)
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	add_led_correction = ("INSERT INTO SmartGreenhouse.LEDCorrection" 
                    	 "(RedValue, GreenValue, BlueValue, Intensity, CorrectionAction_TimeStampStart, CorrectionAction_InstalledCorrectors_CorrectorID)"
                    	 "VALUES(%(RedValue)s, %(GreenValue)s, %(BlueValue)s, %(Intensity)s, %(CorrectionAction_TimeStampStart)s, %(CorrectionAction_InstalledCorrectors_CorrectorID)s);"
                	     )
	data_led_correction = {
	  'RedValue': red_value, 
	  'GreenValue': green_value, 
	  'BlueValue': blue_value, 
	  'Intensity': intensity, 
	  'CorrectionAction_TimeStampStart': start_time, 
	  'CorrectionAction_InstalledCorrectors_CorrectorID': corrector_id,
	}

	cursor.execute(add_led_correction, data_led_correction)
	cnx.commit()
	cursor.close()
	cnx.close()

def turn_correction_off(end_time, corrector_id):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	add_update_correction = ("UPDATE CorrectionAction "
			    	"SET TimeStampEnd = %(end_time)s "
			    	"WHERE InstalledCorrectors_CorrectorID= %(corrector_id)s AND TimeStampEnd IS NULL;"
				)
	data_update_correction = {
		'end_time': end_time,
		'corrector_id':corrector_id,
	}
	cursor.execute(add_update_correction, data_update_correction)
	cnx.commit()
	cursor.close()
	cnx.close()	


def return_desired_conditions_to_arduino(current_time, sensor_id):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	query=("SELECT DesiredCoditionValue, AcceptableRange, ConditionEndTime "
		   "FROM DesiredConditions "
		   "WHERE InstalledSensors_SensorID = %(sensor_id)s AND ConditionStartTime <= %(current_time)s AND ConditionEndTime > %(current_time)s")
	query_data = {
		'sensor_id' : sensor_id,
		'current_time' : current_time,
	}

	cursor.execute(query, query_data)

	for (DesiredCoditionValue, AcceptableRange, ConditionEndTime) in cursor:
		if DesiredCoditionValue==NULL:
			print("No condition set for the current_time")
			
		print("Desired Condition: {}, With range: {} until the {:%d %b %Y}".format(DesiredCoditionValue, AcceptableRange, ConditionEndTime))

	cnx.commit()
	cursor.close()
	cnx.close()	

########### TEST DATA ##############

#Pump on
#read_ser = "6 2018-02-14 10:30:05 2"

#ph on with 22ml equlaiser
#read_ser = "4 2018-02-14 10:31:00 1 22"

#LEDs on
#read_ser = "2 2018-02-14 10:31:30 3 0.9 0.0 0.2 0.7"

#LEDs off
#read_ser = "3 2018-02-14 10:36:00 3"

#Sensor input
#read_ser = "1 2018-02-13 08:52:24 1 22.5 2 520 3 530 4 6.5 5 1004"

#Return setup data for PH
read_ser = "0 2018-02-16 18:15:00 "

print read_ser
connection_type_no, date, time, data = read_ser.split(' ',3)

if (int(connection_type_no) == 0):		#Arduino requests desired consitions to be sent
	current_time, sensor_id
elif (int(connection_type_no) == 1):	#Arduino is sending sensor readings 
	print ("Sensor Input")
	data_array = data.split()
	i = 0
	spaces = data.count(' ')
	while (i <= spaces):
		print "Sensor ID: "
		print data_array[i]
		print "sensor value: "
		print data_array[i+1]
		add_sensor_data(date + ' ' + time, data_array[i], data_array[i+1])
		i = i+2
elif (int(connection_type_no)==2):		#LED correction initiated (lights turned on)
	print "Lights on"
	corrector_id, red_value, green_value, blue_value, intensity = data.split()
	print "red:      " + str((float(red_value)*100)) + "%"
	print "green:    " + str((float(green_value)*100)) + "%"
	print "blue:     " + str((float(blue_value)*100)) + "%"
	print "intensity:" + str((float(intensity)*100)) + "%"

	add_led_correction_data(date + ' ' + time, corrector_id, red_value, green_value, blue_value, intensity)
elif (int(connection_type_no)==3):
	print "Lights off"
	turn_correction_off(date + ' ' + time, data.strip())
elif (int(connection_type_no)==4):
	print "PH equaliser valve open"
	corrector_id, ph_equaliser_volume = data.split()
	print ph_equaliser_volume + "ml of equaliser added"
	add_ph_correction_data(date + ' ' + time, corrector_id, ph_equaliser_volume)
elif (int(connection_type_no)==5):
	print "PH equaliser valve closed"
	turn_correction_off(date + ' ' + time, data.strip())
elif (int(connection_type_no)==6):
	print "Pump on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==7):
	print "Pump off"
	turn_correction_off(date + ' ' + time, data.strip())
elif (int(connection_type_no)==8):
	print "Mixer on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==9):
	print "Mixer off"
	turn_correction_off(date + ' ' + time, data.strip())
elif (int(connection_type_no)==10):
	print "Fan on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==11):
	print "Fan off"
	turn_correction_off(date + ' ' + time, data.strip())


