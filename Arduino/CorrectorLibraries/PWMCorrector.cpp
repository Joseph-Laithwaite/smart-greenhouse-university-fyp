/*
 * PWMCorrector.cpp
 *
 *  Created on: Mar 10, 2018
 *      Author: Joseph Laithwaite
 */

#include "../CorrectorLibraries/PWMCorrector.h"

PWMCorrector::PWMCorrector(uint8_t correctorPin, bool correctorState, uint16_t pwmValue) : StandardCorrector(correctorPin, correctorState) {
	setCorrector(pwmValue);
	if (correctorState==true){
		turnOnCorrector();
	}
}

void PWMCorrector::setCorrector(uint16_t pwmValue){
	this->pwmValue = pwmValue;
}

void PWMCorrector::turnOnCorrector(){
//	Serial.print("Turning corrector pwm on");
	analogWrite(correctorPin, pwmValue);
}


PWMCorrector::~PWMCorrector() {
	// TODO Auto-generated destructor stub
}

