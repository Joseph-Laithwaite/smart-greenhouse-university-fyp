################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ..\makefile.init

RM := del 

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir.mk
-include libraries\Wire\src\utility\subdir.mk
-include libraries\Wire\src\subdir.mk
-include libraries\DHT_sensor_library\subdir.mk
-include libraries\Adafruit_TSL2561\subdir.mk
-include core\core\subdir.mk
-include SensorLibraries\subdir.mk
-include CorrectorLibraries\subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(INO_DEPS)),)
-include $(INO_DEPS)
endif
ifneq ($(strip $(PDE_DEPS)),)
-include $(PDE_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ..\makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
AR += \
C:\Eclipse-Workspace\Smart_Farm4\Release\arduino.ar \

ELF += \
Smart_Farm4.elf \

HEX += \
Smart_Farm4.hex \


# All Target
all: Smart_Farm4

# Tool invocations
Smart_Farm4: $(HEX)
	@echo 'Building target: $@'
	@echo 'Printing size:'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-size" -A "C:/Eclipse-Workspace/Smart_Farm4/Release/Smart_Farm4.elf"
	@echo 'Finished building target: $@'
	@echo ' '

C:\Eclipse-Workspace\Smart_Farm4\Release\arduino.ar: $(AR_OBJ)
	@echo 'Starting archiver'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-gcc-ar" rcs    C:/Eclipse-Workspace/Smart_Farm4/Release/arduino.ar $(AR_OBJ)
	@echo 'Finished building: $@'
	@echo ' '

Smart_Farm4.elf: $(LINK_OBJ) $(AR)
	@echo 'Starting combiner'
	"C:\ProgramData\eclipse\/arduinoPlugin/packages/arduino/tools/avr-gcc/4.9.2-atmel3.5.4-arduino2/bin/avr-gcc" -Wall -Wextra -Os -g -flto -fuse-linker-plugin -Wl,--gc-sections -mmcu=atmega328p -o "C:\Eclipse-Workspace\Smart_Farm4/Release/Smart_Farm4.elf"   $(LINK_OBJ)   C:/Eclipse-Workspace/Smart_Farm4/Release/arduino.ar  "-LC:\Eclipse-Workspace\Smart_Farm4/Release" -lm
	@echo 'Finished building: $@'
	@echo ' '

Smart_Farm4.hex: $(ELF)
	@echo 'Create eeprom image'
	${A.RECIPE.OBJCOPY.EEP.PATTERN}
	${A.RECIPE.OBJCOPY.HEX.PATTERN}
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(C_UPPER_DEPS)$(PDE_DEPS)$(C_DEPS)$(AR)$(CC_DEPS)$(AR_OBJ)$(C++_DEPS)$(LINK_OBJ)$(CXX_DEPS)$(ASM_DEPS)$(HEX)$(INO_DEPS)$(SIZEDUMMY)$(S_UPPER_DEPS)$(ELF)$(CPP_DEPS)
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ..\makefile.targets
