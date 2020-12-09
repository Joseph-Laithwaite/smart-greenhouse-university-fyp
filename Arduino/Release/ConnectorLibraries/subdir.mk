################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
..\ConnectorLibraries\DigitalCorrector.cpp \
..\ConnectorLibraries\LEDCorrector.cpp \
..\ConnectorLibraries\PWMCorrector.cpp \
..\ConnectorLibraries\StandardCorrector.cpp 

LINK_OBJ += \
.\ConnectorLibraries\DigitalCorrector.cpp.o \
.\ConnectorLibraries\LEDCorrector.cpp.o \
.\ConnectorLibraries\PWMCorrector.cpp.o \
.\ConnectorLibraries\StandardCorrector.cpp.o 

CPP_DEPS += \
.\ConnectorLibraries\DigitalCorrector.cpp.d \
.\ConnectorLibraries\LEDCorrector.cpp.d \
.\ConnectorLibraries\PWMCorrector.cpp.d \
.\ConnectorLibraries\StandardCorrector.cpp.d 


# Each subdirectory must supply rules for building sources it contributes
ConnectorLibraries\DigitalCorrector.cpp.o: ..\ConnectorLibraries\DigitalCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '

ConnectorLibraries\LEDCorrector.cpp.o: ..\ConnectorLibraries\LEDCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '

ConnectorLibraries\PWMCorrector.cpp.o: ..\ConnectorLibraries\PWMCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '

ConnectorLibraries\StandardCorrector.cpp.o: ..\ConnectorLibraries\StandardCorrector.cpp
	@echo 'Building file: $<'
	@echo 'Starting C++ compile'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-g++" -c -g -Os -Wall -Wextra -std=gnu++11 -fpermissive -fno-exceptions -ffunction-sections -fdata-sections -fno-threadsafe-statics -flto -mmcu=atmega328p -DF_CPU=16000000L -DARDUINO=10802 -DARDUINO_AVR_NANO -DARDUINO_ARCH_AVR   -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\cores\arduino" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\variants\eightanaloginputs" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_TSL2561\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\Adafruit_Unified_Sensor\1.0.2" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire" -I"C:\ProgramData\eclipse\arduinoPlugin\packages\arduino\hardware\avr\1.6.21\libraries\Wire\src" -I"C:\ProgramData\eclipse\arduinoPlugin\libraries\DHT_sensor_library\1.3.0" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -D__IN_ECLIPSE__=1 -x c++ "$<"  -o  "$@"
	@echo 'Finished building: $<'
	@echo ' '


