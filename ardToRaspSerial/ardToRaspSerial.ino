#include <Servo.h>
#include <Ramp.h>

void manual(int x, int y, int z);
void sendStatus();
void serialEvent();
void setArduinoAngle(Servo servo, int angle);
void rampToAngle(rampDouble& serRamp, Servo& servo, double motorRamp, unsigned long t);


Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;

rampDouble Servo1Ramp;
rampDouble Servo2Ramp;
rampDouble Servo3Ramp;
rampDouble Servo4Ramp;


const unsigned long t = 2000;

////////////////////////////////////////////////////////////////////////////
// const int clampPin = 13;  
////////////////////////////////////////////////////////////////////////////

int servoArmBase = 9;
int servoBaseRotation = 10;
int servoPickerHeight = 11;
int servoGripper = 8;

int potPin = A0; 
int xPort = A1;
int yPort = A2;

int joystickButton = 4;
int gripperSwitch = 2;


int deadband = 10;

int xAngle = 180;
int yAngle = 90;
int zAngle = 90; //this is potentiometer
int gripperAngle = 90;

//tx rx communication variables
String inputString = "";
bool stringComplete = false;
bool isManual = false;


void setup() {
  Serial.begin(115200);
  Serial.println("Initialising Project");

  //assign servos to pins
  Servo1.attach(servoArmBase);
  Servo2.attach(servoBaseRotation);
  Servo3.attach(servoPickerHeight);
  Servo4.attach(servoGripper);

  //initialise manual controlers
  pinMode(joystickButton, INPUT);
  pinMode(gripperSwitch, INPUT);

  //init to start pos
  rampToAngle(Servo1Ramp, Servo1, 180, t);
  rampToAngle(Servo3Ramp, Servo3, 50, t);

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
  // int reading = analogRead(potPin);
  // int angle = map(reading, 0, 1023, 0, 180);
  // Serial.print("Angle: ");
  // Serial.println(angle);
  // Servo1.write(angle);
  int x = analogRead(xPort);
  int y = analogRead(yPort);
  int pickerHeight = analogRead(potPin);
  zAngle = map(pickerHeight, 0, 1023, 0, 180);
  Serial.flush();
  if (stringComplete || isManual) {
    Serial.print("Received command: ");
    Serial.println(inputString);
    if (inputString.startsWith("status")) {
      sendStatus();
    } else if (inputString.startsWith("manual off")) {
      Serial.println("Ending Manual Control");
      sendStatus();
      isManual = false;
    } else if (inputString.startsWith("manual on") || isManual) {
      Serial.println("Starting Manual Control");
      isManual = true;
      manual(x, y, zAngle);
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
        rampToAngle(Servo1Ramp, Servo1, motorAngle, t);
      } else if (motorId == 2) {
        rampToAngle(Servo2Ramp, Servo2, motorAngle, t);
      } else if (motorId == 3) {
//        setArduinoAngle(Servo3, motorAngle);
        Serial.println(Servo3Ramp.getOrigin());
        rampToAngle(Servo3Ramp, Servo3, static_cast<double>(motorAngle), t);
      } else if (motorId == 4) {
        rampToAngle(Servo4Ramp, Servo4, motorAngle, t);
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
      rampToAngle(Servo1Ramp, Servo1, 180, t);
      rampToAngle(Servo3Ramp, Servo3, 50, t);
  
///////////////////////////////////////////////////////////////////////////////
/*
    } else if  (inputString.startsWith("clamp on") {
      turnClampOn();
    } else if (inputString.startsWith("clamp off") {
      turnClampOff();
*/    
///////////////////////////////////////////////////////////////////////////////
    
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

  delay(50);
}

void manual(int x, int y, int zAngle) {
    //x counter go up or down
  if (xAngle < 180 && x > 1023/2 + deadband) {
    xAngle++;
  } else if (xAngle > 0 && x < 1023/2 - deadband) {
    xAngle--;
  } else {
    //do nothing
  }

  //y counter go up or down
  if (yAngle < 180 && y > 1023/2 + deadband) {
    yAngle++;
  } else if (yAngle > 0 && y < 1023/2 - deadband) {
    yAngle--;
  } else {
    //do nothing
  }

  //gripper counter go up or down
  int gripperVal = digitalRead(gripperSwitch);
  if (gripperAngle < 180 && gripperVal == HIGH) {
    gripperAngle++;
  } else if (gripperAngle > 0 && gripperVal == LOW) {
    gripperAngle--;
  }

  int b = digitalRead(joystickButton);
  // Serial.print("Manual Control Data: ");
  // Serial.print(xAngle, DEC);
  // Serial.print(", ");
  // Serial.print(yAngle, DEC);
  // Serial.print(", ");
  // Serial.print(zAngle, DEC);
  // Serial.print(", ");
  // Serial.print(gripperAngle, DEC);
  // Serial.print(", ");
  // Serial.println(b, DEC);

  Servo2.write(xAngle);
  Servo1.write(yAngle);
  Servo3.write(zAngle);
  Servo4.write(gripperAngle);
}

void sendStatus() {
  char buffer[50];
  sprintf(buffer, "%d, %d, %d, %d", xAngle, yAngle, zAngle, gripperAngle);
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
