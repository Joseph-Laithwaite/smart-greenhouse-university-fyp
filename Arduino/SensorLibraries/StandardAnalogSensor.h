/*
 * StandardAnalogSensor.h
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#ifndef STANDARDANALOGSENSOR_H_
#define STANDARDANALOGSENSOR_H_

#include "Sensor.h"

class StandardAnalogSensor {
public:
	StandardAnalogSensor(uint8_t sensorPinNumber, uint8_t powerPinNumber = 255);
	virtual ~StandardAnalogSensor();
	uint8_t getSensorPinNumber();
	uint8_t getPowerPinNumber();
	virtual int getSensorValue();

protected:
	uint8_t sensorPinNumber;
	uint8_t powerPinNumber;
};

#endif /* STANDARDANALOGSENSOR_H_ */
