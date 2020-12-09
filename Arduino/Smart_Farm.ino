#include "Arduino.h"
#include "SensorLibraries/Sensor.h"
#include "SensorLibraries/DHT22Sensor.h"
#include "SensorLibraries/I2cSensor.h"
#include "SensorLibraries/RelayPoweredAnalogSensor.h"
#include "SensorLibraries/StandardAnalogSensor.h"

#include "CorrectorLibraries/StandardCorrector.h"
#include "CorrectorLibraries/PWMCorrector.h"

String waitForInput(){
    while(!Serial.available());
    return Serial.readString();
}

void decodeAndExecuteSensorRead(String instruction){
	  //Serial.println("Sensor read about to occur");
	  //String sensorTypeID = instruction.substring(1,4);
	  switch((instruction.substring(1,4)).toInt()){		//switch between sensor types
	  	  case(1):      //PH
			  {
		  	  	uint8_t sensorPin = uint8_t(instruction.substring(4,7).toInt()); //sensor pin
	  	  	  	uint8_t powerPin = uint8_t(instruction.substring(7,10).toInt());  //power pin
	  	  	  	StandardAnalogSensor phSensor = StandardAnalogSensor(sensorPin, powerPin);
	  	  	  	//Serial.print("PH: ");
	  	  	  	Serial.println(phSensor.getSensorValue());
//	  	  	  	delete phSensor;
			  break;
			  }
	      case(2):      //WaterLevel
				{
				RelayPoweredAnalogSensor waterLevelSensor = RelayPoweredAnalogSensor(uint8_t(instruction.substring(4,7).toInt()), uint8_t(instruction.substring(7,10).toInt()), uint8_t(instruction.substring(10,13).toInt())) ;
			  	//Serial.print("Water Level (cm): ");
				Serial.println(waterLevelSensor.getSensorValue());
				}

	        break;
	      case(3):    //Light
				{
	    	  	  I2cSensor lightSensor = I2cSensor(uint8_t(instruction.substring(4,7).toInt()), bool(instruction.substring(7,8).toInt()));
	    	  	  //Serial.print("Light: ");
	    	  	  Serial.println(lightSensor.getSensorValue());
	    	  	  }
	        break;
	      case(4):	//temp
				{
		    	//Serial.println("Temp");
	    	  	//Serial.print("Sensor Pin ");
	    	  	//Serial.println(instruction.substring(4,7).toInt());
	    	  	//Serial.print("Power Pin ");
	    	  	//uint8_t powerPin = uint8_t(instruction.substring(7,10).toInt());
	    	  	//Serial.println(powerPin);
	    	  	//Serial.println(uint8_t(instruction.substring(4,7).toInt()));
				DHT22Sensor tempHumidSensor = DHT22Sensor(uint8_t(instruction.substring(4,7).toInt()), uint8_t(instruction.substring(7,10).toInt()), false) ;
				//Serial.print("Temp (or humidity): ");
				Serial.println(tempHumidSensor.getSensorValue());
				}
		        break;
	      case(5):     //Humidity
				{
	    	  	Serial.println("Humidity");
				DHT22Sensor tempHumidSensor = DHT22Sensor(uint8_t(instruction.substring(4,7).toInt()), uint8_t(instruction.substring(7,10).toInt()), true) ;
				Serial.println(tempHumidSensor.getSensorValue());
				}
	      break;

	      //default:
	    	  //Serial.println("Unknown sensor");
	  	 }
}

void decodeAndExecuteCorrectorAction(String instruction){
	//Serial.println("Correction action about to take place");
	switch((instruction.substring(1,4)).toInt()){
	case(1):{	//on for a short period of time eg.PH Equaliser valve or water mixer
//		  Serial.print("Pin number ");
		  uint8_t pinNum = uint8_t(instruction.substring(4,7).toInt());
//		  Serial.print(pinNum);
		  int onTime = instruction.substring(7,12).toInt();
//		  Serial.print(" on for ");
//		  Serial.print(String(onTime));
//		  Serial.println(" m seconds");
		  StandardCorrector corrector = StandardCorrector(uint8_t(instruction.substring(4,7).toInt()), true);	//initialise and turn on equaliser valve
		  delay(instruction.substring(7,12).toInt());
		  corrector.turnOffCorrector();
		  Serial.println("Correction Made");
		  break;
	}
	case(2): {	//On or Off, eg. fan & pump
//		  Serial.print("Corrector at pin number ");
//		  Serial.print(uint8_t(instruction.substring(4,7).toInt()));
//		  if (bool(instruction.substring(7,8).toInt())==true){
//			  Serial.print(" turned on");
//		  }else{
//			  Serial.print(" turned off");
//		  }
		  StandardCorrector corrector = StandardCorrector(uint8_t(instruction.substring(4,7).toInt()), bool(instruction.substring(7,8).toInt()));	//initialise and turn on equaliser valve
		  Serial.println("Correction Made");
		  break;
	}
	case(3):{			//LEDs PWM corrector On
		  //Serial.println("PWM corrector on");
		  PWMCorrector pwmCorrector = PWMCorrector(uint8_t(instruction.substring(4,7).toInt()),  bool(instruction.substring(12,13).toInt()), uint16_t(instruction.substring(7,12).toInt()));
		  Serial.println("Correction Made");
	}
	}
}

#ifdef __arm__
// should use uinstd.h to define sbrk but Due causes a conflict
extern "C" char* sbrk(int incr);
#else  // __ARM__
extern char *__brkval;
#endif  // __arm__

int freeMemory() {
  char top;
#ifdef __arm__
  return &top - reinterpret_cast<char*>(sbrk(0));
#elif defined(CORE_TEENSY) || (ARDUINO > 103 && ARDUINO != 151)
  return &top - __brkval;
#else  // __arm__
  return __brkval ? &top - __brkval : &top - __malloc_heap_start;
#endif  // __arm__
}

void decodeSensorOrCorrector(String instruction){
  if(instruction.substring(0,1) == "s"){		//communication code is s (sensor read)
	  decodeAndExecuteSensorRead(instruction);
  }else if(instruction.substring(0,1) == "c"){		//communication code is  (correction action)
	  decodeAndExecuteCorrectorAction(instruction);
  }else if(instruction.substring(0,1) == "m"){
	  Serial.println(freeMemory());
  }
}
/*
void setupLoop(){
  String input;
  int count=-1;
  pinMode(13, OUTPUT);
  while(input != "FINIHED"){
    input = waitForInput();
    count = count + 1;
    Serial.print(input + " recieved");
    decodeSensorOrCorrector(input);
  }
  Serial.print(count + " instructions recieved");
}
*/

void setup() {
  Serial.begin(9600);
  Serial.print("Arduino Ready\n");
}


//int i;
static String input;

void loop() {
  input = waitForInput();
  decodeSensorOrCorrector(input);
}
