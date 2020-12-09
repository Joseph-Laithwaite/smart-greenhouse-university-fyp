/*
 * Sensor.cpp
 *
 *  Created on: 19 Feb 2018
 *      Author: josephlaithwaite
 */

#include "Sensor.h"

Sensor::Sensor(uint8_t sensorID) {
	 this->sensorID = sensorID;
}

Sensor::~Sensor() {
	// TODO Auto-generated destructor stub
}



uint8_t	Sensor::getSensorID(){
	return sensorID;
}


int Sensor::getSensorValue(){
	return 0;
}
