/*
 * RelayPoweredAnalogSensor.h
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#ifndef RELAYPOWEREDANALOGSENSOR_H_
#define RELAYPOWEREDANALOGSENSOR_H_

#include "StandardAnalogSensor.h"

class RelayPoweredAnalogSensor: public StandardAnalogSensor {
public:
	RelayPoweredAnalogSensor(uint8_t sensorPinNumber, uint8_t powerPinNumber, uint8_t relayPinNumber);
	virtual ~RelayPoweredAnalogSensor();

	uint8_t getRelayPin();
	int getSensorValue();

protected:
	uint8_t relayPinNumber;
};

#endif /* RELAYPOWEREDANALOGSENSOR_H_ */
