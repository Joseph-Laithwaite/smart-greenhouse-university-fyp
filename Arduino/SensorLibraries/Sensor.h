/*
 * Sensor.h
 *
 *  Created on: 19 Feb 2018
 *      Author: josephlaithwaite
 */
#include <Arduino.h>

#ifndef SENSOR_H_
#define SENSOR_H_

class Sensor {
public:
	Sensor(uint8_t sensorID);
	uint8_t	getSensorID();
	virtual int getSensorValue();
	virtual ~Sensor();
protected:
	uint8_t sensorID;
};

#endif /* SENSOR_H_ */
