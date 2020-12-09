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


#ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
#ser.baudrate=9600


#read_ser=ser.readline()
read_ser = "0 2017,11,02,19,47,03 1 4.5 2 33.6"

print(read_ser)
type_no, time, data = read_ser.count(' ',2)

if(type_no == 0):
	inputs = data.count(' ')
	data_array = data.split()
	i = 0
	while (i <= inputs):
		print("Sensor ID: ")
		print(data_array[i])
		print("sensor value: ")
		print(data_array[i+1])
		add_sensor_data(time, data_array[i], data_array[i+1])
		#type_no, time, ph, water_volume, int_temp, ext_temp, int_humidity, int_light, ext_light = read_ser.split()
		#first two inputs give contect for all readings, type & time
		#the subsequent inputs are pairs with the sensorID & the sensor Reading.





def add_sensor_data(time, sensor_id, sensor_reading)
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
