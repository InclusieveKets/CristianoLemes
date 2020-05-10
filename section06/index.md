---
layout: default
title: Section 06 - Arduino
---

# Arduino

The class took place by Zoom because of the Corona Situation.
The topic of this section was Arduino and we have gotten a set of sensors and one arduino to do some exercises in the class.
First it was presented a bit of the hystory of Arduino, which the first version was released at 2005.
Arduino is an open source and open hardware that enable to connect IoT sensors and connect them designing solutions for tasks from the real word.
There are differents types of Arduino varying from size and performance, allowing to choose a more suitable board depending of the type of project that is being implemented.
The real examples gave a very good overview of the topic allowing to picture ideas for the final project.

The program in Arduino is split into two main functions: setup() and loop().
The former one is responsible to prepare the board initializing variables and setting the pins that will be used from the Arduino.
The second one is the function that is executed until the Arduino is swicthed off.
It contains the logic of the eletronic system being designed.

One of the exercises done in this class, I have designed a very simple program that move forward and backward one servo in 150 degrees.
The function setup() adjust the initial position of the servo to 90 degrees and set the pin in the Arduino where the servo is connected.
The function loop() contains the code that move forward and backward the servo.
The code bellow give an overview of this simple example.
It is very important to connect the Arduino correctly too guarantee that the circuit will run and the Arduino will actually do what is being programmed for.
If the parts is not connected correctly, the Arduino will not work.

```arduino
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
```

## Websites

[Arduino IDE](https://www.arduino.cc/en/Main/Software)
[Examples of Arduino code](https://ingegno.be/realisations/blockly4arduino.html)
[Drag and drop design of Arduino code](https://blokkencode.ingegno.be/)
[Virtual Arduino to test the program](https://www.tinkercad.com/)
