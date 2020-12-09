/*
 * DHT22Sensor.cpp
 *
 *  Created on: 9 Mar 2018
 *      Author: josephlaithwaite
 */

#include "DHT22Sensor.h"

DHT22Sensor::DHT22Sensor(uint8_t sensorPinNumber, uint8_t powerPinNumber, bool humidityOrTemp) : StandardAnalogSensor(sensorPinNumber, powerPinNumber) {
	// TODO Auto-generated constructor stub
	//Serial.println(String(sensorPinNumber) + " " + String(powerPinNumber) + " " + String(humidityOrTemp));
	this->humidityOrTemp = humidityOrTemp;
}

DHT22Sensor::~DHT22Sensor() {
	// TODO Auto-generated destructor stub
}

int DHT22Sensor::getSensorValue(){
	//int err = 0;
	if (humidityOrTemp==true){
		//Serial.println("Getting humidity ");
		float humidity;
		//err =
		tempHumidSensor.read2(getSensorPinNumber(), NULL, &humidity, NULL);
		return int(humidity*10);
	}else{
		//Serial.println("Getting temperature ");

		float temperature;
		//err =
		tempHumidSensor.read2(getSensorPinNumber(), &temperature, NULL, NULL);
		return int(temperature*10);
	}
}
