/*
 * RelayPoweredAnalogSensor.cpp
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#include "RelayPoweredAnalogSensor.h"

RelayPoweredAnalogSensor::RelayPoweredAnalogSensor(uint8_t sensorPinNumber, uint8_t powerPinNumber, uint8_t relayPinNumber) : StandardAnalogSensor(sensorPinNumber, powerPinNumber) {
	this -> relayPinNumber = relayPinNumber;
}

uint8_t RelayPoweredAnalogSensor::getRelayPin(){
	return relayPinNumber;
}

int RelayPoweredAnalogSensor::getSensorValue(){
	pinMode(relayPinNumber,OUTPUT);
	digitalWrite(relayPinNumber, HIGH);
	delay(100);
	int currentRawInput = StandardAnalogSensor::getSensorValue();
	digitalWrite(relayPinNumber, LOW);
	pinMode(relayPinNumber, OUTPUT);
	pinMode(relayPinNumber, INPUT);
	digitalWrite(relayPinNumber, LOW);

	return currentRawInput;
}

RelayPoweredAnalogSensor::~RelayPoweredAnalogSensor() {
	// TODO Auto-generated destructor stub
}

