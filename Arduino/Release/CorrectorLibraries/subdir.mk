################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
..\CorrectorLibraries\PWMCorrector.cpp \
..\CorrectorLibraries\StandardCorrector.cpp 

LINK_OBJ += \
.\CorrectorLibraries\PWMCorrector.cpp.o \
.\CorrectorLibraries\StandardCorrector.cpp.o 

CPP_DEPS += \
.\CorrectorLibraries\PWMCorrector.cpp.d \
.\CorrectorLibraries\StandardCorrector.cpp.d 


# Each subdirectory must supply rules for building sources it contributes
CorrectorLibraries\PWMCorrector.cpp.o: ..\CorrectorLibraries\PWMCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '

CorrectorLibraries\StandardCorrector.cpp.o: ..\CorrectorLibraries\StandardCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '


