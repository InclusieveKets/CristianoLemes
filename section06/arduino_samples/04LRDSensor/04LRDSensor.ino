int analog_var;
boolean state_push_btn;
int PUSH_BTN = 4;
int LED = 13;
int AnaSensor1 = A5;

void setup() {
  pinMode(PUSH_BTN, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(AnaSensor1, INPUT);
  Serial.begin(9600);

  Serial.println("Hello World!");

}

void loop() {
  analog_var = analogRead(AnaSensor1);
  state_push_btn = digitalRead(PUSH_BTN);
  Serial.print("state=");
  Serial.println(state_push_btn);
  Serial.print("LDR=");
  Serial.println(analog_var);
  if (analog_var > 900) {
    digitalWrite(LED, HIGH);
  } else {
    digitalWrite(LED, LOW);
  }
  //delay(1000);

}
