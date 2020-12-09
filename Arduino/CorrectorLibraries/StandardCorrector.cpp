/*
 * StandardCorrector.cpp
 *
 *  Created on: Mar 10, 2018
 *      Author: Joseph Laithwaite
 */

#include "../CorrectorLibraries/StandardCorrector.h"

StandardCorrector::StandardCorrector(uint8_t correctorPin, bool correctorState) {
	this->correctorPin = correctorPin;
	this->correctorState = correctorState;
	if (correctorState==true){
		turnOnCorrector();
	}else{
		turnOffCorrector();
	}
}

void StandardCorrector::turnOnCorrector(){
	pinMode(correctorPin, OUTPUT);
	digitalWrite(correctorPin,HIGH);
//	Serial.println("Corrector ON");
}

void StandardCorrector::turnOffCorrector(){
	pinMode(correctorPin, INPUT);
	pinMode(correctorPin, OUTPUT);
	digitalWrite(correctorPin,LOW);
//	Serial.println("Corrector OFF");
}

bool StandardCorrector::getCorrectorState(){
	return correctorState;
}

void StandardCorrector::setCorrector(){}


StandardCorrector::~StandardCorrector() {
	// TODO Auto-generated destructor stub
}

