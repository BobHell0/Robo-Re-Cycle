#include <Servo.h>
#include <Ramp.h>

#include "Encoder.hpp"
#include "Motor.hpp"
#include "PIDController.hpp"
#include "BangBangController.hpp"

void manual(int x, int y, int z);
void sendStatus();
void serialEvent();
void setArduinoAngle(Servo servo, int angle);
void rampToAngle(rampDouble& serRamp, Servo& servo, double motorRamp, unsigned long t);
void rotate(float target, float dir);


Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;

rampDouble Servo1Ramp;
rampDouble Servo2Ramp;
rampDouble Servo3Ramp;
rampDouble Servo4Ramp;


const unsigned long t = 2000;

//base motor setup
//using https://www.pololu.com/product/2135
#define MOT1PWM 5 // PIN 5 is a PWM pin
#define MOT1DIR 6 // Enable pin
mtrn3100::Motor motor(MOT1PWM,MOT1DIR);

#define EN_A 2 // PIN 2 is an interupt
#define EN_B 4 // PIN 4 is for dir
mtrn3100::Encoder encoder(EN_A, EN_B);

mtrn3100::BangBangController controller(200, 0.01);

////////////////////////////////////////////////////////////////////////////
// const int clampPin = 13;  
////////////////////////////////////////////////////////////////////////////

int servoArmBase = 9;
int servoPickerHeight = 11;
//int servoGripper = 8; //This is a spare pin in case something goes wrong and needs to be changed

int xAngle = 0;
int yAngle = 0;

//tx rx communication variables
String inputString = "";
bool stringComplete = false;
bool isManual = false;


void setup() {
  Serial.begin(115200);
  Serial.println("Initialising Project");

  //assign servos to pins
  Servo1.attach(servoArmBase);
  Servo3.attach(servoPickerHeight);
  // Servo4.attach(servoGripper); //This is a spare servo port in case something goes wrong and needs to be changed

  //init to start pos
  rampToAngle(Servo1Ramp, Servo1, 40, t);
  rampToAngle(Servo3Ramp, Servo3, 180, t);
  xAngle = 40;
  yAngle = 180;

//////////////////////////////////////////////////////////////////////////
  // turnClampOff();
//////////////////////////////////////////////////////////////////////////

  while (!Serial) {
	;
  }
//  while (Serial.available() <= 0){
//    sendStatus();
//    delay(300);
//  }
  // Servo3.write(zAngle); //This should be commented out for potentiometer
}

void loop() {
  // int x = analogRead(xPort);
  // int y = analogRead(yPort);
  // int pickerHeight = analogRead(potPin);
  // zAngle = map(pickerHeight, 0, 1023, 0, 180);
  Serial.flush();

  if (stringComplete || isManual) {
	Serial.print("Received command: ");
	Serial.println(inputString);
	if (inputString.startsWith("status")) {
	  sendStatus();
	} else if (inputString.startsWith("setMotor ")) {
	  //assuming command is as so: setMotor Servo1, 90
	  String tempStr = inputString;
	  tempStr.remove(0,9);
	  int commaIndex = tempStr.indexOf(',');
	  int motorId = tempStr.substring(0, commaIndex).toInt(); // extract motor ID
	  int motorAngle = tempStr.substring(commaIndex + 2).toInt(); // extract motor angle
	  Serial.print("writing servo ");
	  Serial.print(motorId);
	  Serial.print(" to angle ");
	  Serial.println(motorAngle);

	  if (motorId == 1) {
		rampToAngle(Servo1Ramp, Servo1, static_cast<double>(motorAngle), t);
		yAngle = motorAngle;
	  } else if (motorId == 3) {
		rampToAngle(Servo3Ramp, Servo3, static_cast<double>(motorAngle), t);
		xAngle = motorAngle;
	  } else if (motorId == 4) {
		// rampToAngle(Servo4Ramp, Servo4, static_cast<double>(motorAngle), t);
		//uncomment for extra Servo
	  } else {
		Serial.println("Invalid motor ID");
	  }
	} else if (inputString.startsWith("reset")) {
	  Serial.print("writing servo ");
	  Serial.print(1);
	  Serial.print(" to angle ");
	  Serial.println(180);
	  Serial.print("writing servo ");
	  Serial.print(2);
	  Serial.print(" to angle ");
	  Serial.println(90);
	  rampToAngle(Servo1Ramp, Servo1, 40, t);
	  rampToAngle(Servo3Ramp, Servo3, 180, t);
	  xAngle = 40;
	  yAngle = 180;
  
///////////////////////////////////////////////////////////////////////////////
/*
	} else if  (inputString.startsWith("clamp on") {
	  turnClampOn();
	} else if (inputString.startsWith("clamp off") {
	  turnClampOff();
*/    
///////////////////////////////////////////////////////////////////////////////
	
	} else if (inputString.startsWith("rotate ")) {
	  //assuming command is as so: rotate x, dir . x = (angle in degrees) dir = 1 (clockwise), -1 (anti clockwise)
	  String tempStr = inputString;
	  tempStr.remove(0,7);
	  int commaIndex = tempStr.indexOf(',');

	  float motorAngle = tempStr.substring(0, commaIndex).toFloat(); // extract motor angle
		float dir = tempStr.substring(commaIndex + 2).toFloat(); //extract 
	  Serial.print("rotating machine to angle ");
	  Serial.print(motorAngle);
		if (dir == -1.0) {
			Serial.println(" counterclockwise");
		} else {
			Serial.println(" clockwise");
		}

		rotate(motorAngle, dir);

	} else {
	  Serial.println("invalid command");
	}
	//reset string
	stringComplete = false;
	inputString = "";
  }
  
  if (Serial.available() > 0) {
	serialEvent();
  }

  delay(25);
}

void sendStatus() {
  char buffer[50];
  sprintf(buffer, "%d, %d, %d, %d", xAngle, yAngle);
  Serial.println(buffer);
}

void serialEvent() {
  while (Serial.available()) {
	char inChar = (char)Serial.read();
	inputString += inChar;
	if (inChar = '\n') {
	  stringComplete = true;
	}
  }
}

void setArduinoAngle(Servo servo, int angle) {
  servo.write(angle);
}

void rampToAngle(rampDouble& serRamp, Servo& servo, double motorRamp, unsigned long t) {
  double currPos = servo.read();
  serRamp.go(currPos, 0, NONE, ONCEFORWARD);
  serRamp.go(motorRamp, t, LINEAR, ONCEFORWARD);

  while (serRamp.isRunning()) {
//    Serial.println(serRamp.update());
	setArduinoAngle(servo, serRamp.update());
  }
}

void rotate(float target, float dir) {

  target = dir * abs(target) * PI / 180.0;
	controller.zeroAndSetTarget(encoder.getRotation(), target);


	while (true) {

		float temp = controller.compute(encoder.getRotation());

		if (fabs(controller.getError()) < 0.01) {
        motor.setPWM(0);
        Serial.println("Target reached");
				break;
    } else {
        motor.setPWM(temp);
    }

		encoder.readEncoder();
		delay(10);
	}
}

////////////////////////////////////////////////////////////////////////////
/*
void turnClampOn() {
  clampState = true;
  digitalWrite(clampPin, HIGH); 
  Serial.println("Clamp ON");
}

void turnClampOff() {
  clampState = false;
  digitalWrite(clampPin, LOW);  
  Serial.println("Clamp OFF");
}
*/
/////////////////////////////////////////////////////////////////////////////
