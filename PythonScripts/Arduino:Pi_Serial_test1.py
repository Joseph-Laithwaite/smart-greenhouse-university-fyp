import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyUSB0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600


read_ser=ser.readline()
print(read_ser)
if(read_ser=="Hello From Arduino!"):
blink(11)

