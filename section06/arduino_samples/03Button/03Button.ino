boolean state_btn;
int PUSH_BTN = 4;
int LED = 13;

void setup() {
  pinMode(PUSH_BTN, INPUT);
  pinMode(LED, OUTPUT);
  Serial.begin(9600);

  Serial.println("Arduino Ready...");

}

void loop() {
  state_btn = digitalRead(PUSH_BTN);
  Serial.print("state_btn: ");
  Serial.println(state_btn);
  if (state_btn) {
    digitalWrite(LED, HIGH);
  } else {
    digitalWrite(LED, LOW);
  }
  delay(1000);

}
