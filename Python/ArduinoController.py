# ArduinoController.py
# ---Import Libraries
import mysql.connector
# Database connection

import serial
# Connection with arduino
import time
# Sleep function
import arduino_sensor_corrector_control as ascc


config = {
   'user': 'joseph',
   'password': 'passcode',
   'host': 'localhost',
   'database': 'SmartGreenhouse_2',
   'raise_on_warnings': True,
}

arduino = serial.Serial("/dev/ttyUSB0", 9600)
# change ACM number as found from ls /dev/tty*
arduino.baudrate = 9600
time.sleep(2)
# Wait for arduino to restart after connecting

cnx = mysql.connector.connect(**config)


read_ser = arduino.readline()
# get input from arduino

while read_ser != b'Arduino Ready\n':
   read_ser = arduino.readline()
   print("Arduino not ready")
   # print error if arduino isn't ready

print("Arduino ready")

region_id = 1
# region_id = ser.readline()   Get region ID from Arduino

ascc.turn_all_correctors_off(region_id, cnx, arduino)
# As all correctors are on on startup, they must be turned off.

while arduino.isOpen():
   ascc.get_all_sensor_data_in_region(region_id, cnx, arduino)
   ascc.carry_out_corrections_on_all_modules(region_id, cnx, arduino)
   print("")
   # arduino.write("m")
   # Requests the dynamic memory space left on the Arduino, used for debugging
   # print(arduino.readline())
   # Displays the free memory


arduino.close()
# close serial connection when the program ends
