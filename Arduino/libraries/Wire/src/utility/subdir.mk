################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src\utility\twi.c 

C_DEPS += \
.\libraries\Wire\src\utility\twi.c.d 

LINK_OBJ += \
.\libraries\Wire\src\utility\twi.c.o 


# Each subdirectory must supply rules for building sources it contributes
libraries\Wire\src\utility\twi.c.o: C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src\utility\twi.c
	@echo 'Building file: $<'
	@echo 'Starting C compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-gcc" -c -g -Os -Wall -Wextra -std=gnu11 -ffunction-sections -fdata-sections -flto -fno-fat-lto-objects -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '


