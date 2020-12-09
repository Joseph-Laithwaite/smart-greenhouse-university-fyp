/*
 * PWMCorrector.h
 *
 *  Created on: Mar 10, 2018
 *      Author: Joseph Laithwaite
 */

#ifndef PWMCORRECTOR_H_
#define PWMCORRECTOR_H_

#include "../CorrectorLibraries/StandardCorrector.h"

class PWMCorrector: public StandardCorrector {
public:
	PWMCorrector(uint8_t correctorPin, bool correctorState, uint16_t pwmValue);
	void setCorrector(uint16_t pwmValue);
	void turnOnCorrector();
	virtual ~PWMCorrector();
private:
	uint16_t pwmValue;
};

#endif /* PWMCORRECTOR_H_ */
