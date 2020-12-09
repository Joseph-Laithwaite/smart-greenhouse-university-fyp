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


def add_sensor_data(time, sensor_id, sensor_reading):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
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
	add_led_correction = ("SmartGreenhouse.LEDCorrection" 
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

	cursor.execute(add_ph_correction, data_ph_correction)
	cnx.commit()
	cursor.close()
	cnx.close()

#ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
#ser.baudrate=9600


#read_ser=ser.readline()
read_ser = "0 2018-02-13 08:52:24 1 22.5 2 520 3 530 4 6.5 5 1004"

print read_ser
connection_type_no, date, time, data = read_ser.split(' ',3)
spaces = data.count(' ')

if (int(connection_type_no) == 0):
	print ("Sensor Input")
	data_array = data.split()
	i = 0
	while (i <= spaces):
		print "Sensor ID: "
		print data_array[i]
		print "sensor value: "
		print data_array[i+1]
		add_sensor_data(date + ' ' + time, data_array[i], data_array[i+1])
		i = i+2
elif (int(connection_type_no)==1):
	print "Lights on"
	corrector_id, red_value, green_value, blue_value, intensity = data.split()
	add_led_correction_data(date + ' ' + time, corrector_id, red_value, green_value, blue_value, intensity)
elif (int(connection_type_no)==2):
	print "Lights off"
elif (int(connection_type_no)==3):
	print "PH equaliser valve open"
	corrector_id, ph_equaliser_volume = data.split()
	add_ph_correction_data(date + ' ' + time, corrector_id, ph_equaliser_volume)
elif (int(connection_type_no)==4):
	print "PH equaliser valve closed"
elif (int(connection_type_no)==5):
	print "Pump on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==6):
	print "Pump off"
elif (int(connection_type_no)==7):
	print "Mixer on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==8):
	print "Mixer off"
elif (int(connection_type_no)==9):
	print "Fan on"
	add_start_correction_action_data(date + ' ' + time, data.strip())
elif (int(connection_type_no)==10):
	print "Fan off"
	