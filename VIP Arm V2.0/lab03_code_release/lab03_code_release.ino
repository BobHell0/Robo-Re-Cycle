#include "Encoder.hpp"
#include "Motor.hpp"
#include "PIDController.hpp"
#include "BangBangController.hpp"

#define MOT1PWM 9 // PIN 9 is a PWM pin
#define MOT1DIR 10
mtrn3100::Motor motor(MOT1PWM,MOT1DIR);

#define EN_A 2 // PIN 2 is an interupt
#define EN_B 4
mtrn3100::Encoder encoder(EN_A, EN_B);

#define deadband float(5)
static bool trigger = false;

float target = PI;

mtrn3100::BangBangController controller(120, 0.2);

void setup() {
  Serial.begin(115200);
  Serial.println(encoder.getRotation());
  controller.zeroAndSetTarget(encoder.getRotation(), target); // Set the target as 2 Radians
}

void loop() {


  float temp = controller.compute(encoder.getRotation());
  Serial.println(encoder.getRotation());
  if (encoder.getRotation() >= target) {
    motor.setPWM(0);
    Serial.print("complete");
  } else {
    motor.setPWM(temp);
  }

  encoder.readEncoder();
  delay(10);
  // motor.setPWM(120);
}
