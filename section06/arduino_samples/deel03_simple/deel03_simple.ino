#include <Servo.h>

int i;
int servo_ex = 9;

Servo myServoservo_ex;

void setup() {
  myServoservo_ex.attach(9);
  Serial.begin(9600);

  myServoservo_ex.write(90);
  delay(500);
  Serial.println("Arduino Ready...");

}

void loop() {
  for (i = 0; i <= 150; i += 10) {
    myServoservo_ex.write(i);
    delay(40);
  }
  for (i = 150; i >= 0; i -= 10) {
    myServoservo_ex.write(i);
    delay(40);
  }

}
