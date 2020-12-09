/*
 * I2cSensor.h
 *
 *  Created on: Mar 9, 2018
 *      Author: Joseph Laithwaite
 */

#ifndef I2CSENSOR_H_
#define I2CSENSOR_H_

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_TSL2561_U.h>
#include "Sensor.h"

class I2cSensor{
public:
	I2cSensor(uint8_t sensorID, bool floatOrLow);
	int getSensorValue();
	virtual ~I2cSensor();
private:
	Adafruit_TSL2561_Unified * tsl;
};

#endif /* I2CSENSOR_H_ */
