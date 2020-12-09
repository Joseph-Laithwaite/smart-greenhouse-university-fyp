/*
 * StandardCorrector.h
 *
 *  Created on: Mar 10, 2018
 *      Author: Joseph Laithwaite
 */

#ifndef STANDARDCORRECTOR_H_
#define STANDARDCORRECTOR_H_

#include "Arduino.h"

class StandardCorrector {
public:
	StandardCorrector(uint8_t correctorPin, bool correctorState = false);
	virtual ~StandardCorrector();
	virtual void turnOnCorrector();
	void turnOffCorrector();
	bool getCorrectorState();
	virtual void setCorrector();
protected:
	uint8_t correctorPin;
	bool correctorState;
};

#endif /* STANDARDCORRECTOR_H_ */
