/*
 * I2cSensor.cpp
 *
 *  Created on: Mar 9, 2018
 *      Author: Joseph Laithwaite
 */

#include "I2cSensor.h"

I2cSensor::I2cSensor(uint8_t sensorID, bool floatOrLow){
	//Serial.println(String(sensorID) + " " + String(floatOrLow));
	if (floatOrLow==true){
		tsl  = new Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, sensorID);
	}else{
		tsl  = new Adafruit_TSL2561_Unified(TSL2561_ADDR_LOW, sensorID);
	}
	tsl->enableAutoRange(true);            /* Auto-gain ... switches automatically between 1x and 16x */
	tsl->setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
}

int I2cSensor::getSensorValue(){
	sensors_event_t event;
	tsl->getEvent(&event);
	return event.light;
}

I2cSensor::~I2cSensor() {
	delete tsl;
	// TODO Auto-generated destructor stub
}
