/*
 * StandardAnalogSensor.cpp
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#include "StandardAnalogSensor.h"

StandardAnalogSensor::StandardAnalogSensor(uint8_t sensorPinNumber, uint8_t powerPinNumber) {
	// TODO Auto-generated constructor stub
	 this->sensorPinNumber = sensorPinNumber;
	 this->powerPinNumber = powerPinNumber;
	 pinMode(sensorPinNumber,INPUT);
}

StandardAnalogSensor::~StandardAnalogSensor() {
	// TODO Auto-generated destructor stub
}

int StandardAnalogSensor::getSensorValue(){
	int currentRawInput;
	if (powerPinNumber==255){		//code for no power pin used
		currentRawInput =  analogRead(sensorPinNumber);
	}else{
		pinMode(powerPinNumber,OUTPUT);
		digitalWrite(powerPinNumber, HIGH);
		delay(500);
		currentRawInput =  analogRead(sensorPinNumber);
		delay(300);
		pinMode(powerPinNumber, OUTPUT);
		pinMode(powerPinNumber, INPUT);
		digitalWrite(powerPinNumber, LOW);
	}
	return currentRawInput;
}

uint8_t StandardAnalogSensor::getSensorPinNumber(){
	return sensorPinNumber;
}

uint8_t StandardAnalogSensor::getPowerPinNumber(){
	return powerPinNumber;
}
