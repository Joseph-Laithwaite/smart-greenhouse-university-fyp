/*
 * DHT22Sensor.h
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#ifndef DHT22SENSOR_H_
#define DHT22SENSOR_H_

#include "SimpleDHT.h"
#include "StandardAnalogSensor.h"

class DHT22Sensor: public StandardAnalogSensor {
public:
	DHT22Sensor(uint8_t sensorPinNumber, uint8_t powerPinNumber, bool humidityOrTemp);
	virtual ~DHT22Sensor();
	virtual int getSensorValue();

private:
	SimpleDHT22 tempHumidSensor;
	bool humidityOrTemp;
};

#endif /* DHT22SENSOR_H_ */
