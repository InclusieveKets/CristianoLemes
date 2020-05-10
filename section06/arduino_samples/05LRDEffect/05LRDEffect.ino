int analog_var;
boolean state_push_btn;
int PUSH_BTN = 4;
int LED = 13;
int AnaSensor1 = A5;

int ard_effect0_status = -1;
unsigned long ard_effect0_start, ard_effect0_time;
#define EFFECT0_PERIOD 1000

// Describe this function...
void write_debug_output() {
  //Variables of this effect are reffered to with ard_effect0
  boolean restart = false;
  ard_effect0_time = millis() - ard_effect0_start;
  if (ard_effect0_time > EFFECT0_PERIOD) {
    //end effect, make sure it restarts
    if (ard_effect0_status > -1) {
    }
    restart = true;
    ard_effect0_status = -1;
    ard_effect0_start = ard_effect0_start + ard_effect0_time;
    ard_effect0_time = 0;
  }
  if (not restart && ard_effect0_status == -1) {
    ard_effect0_status = 0;
    ard_effect0_start = ard_effect0_start + ard_effect0_time;
    ard_effect0_time = 0;
  Serial.print("state=");
  Serial.println(state_push_btn);
  Serial.print("LDR=");
  Serial.println(analog_var);
  }
}



void setup() {
  pinMode(PUSH_BTN, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(AnaSensor1, INPUT);
  Serial.begin(9600);
  ard_effect0_status = -1;
  ard_effect0_start = millis();


  Serial.println("Hello World!");

}

void loop() {
  analog_var = analogRead(AnaSensor1);
  state_push_btn = digitalRead(PUSH_BTN);
  if (analog_var > 850) {
    digitalWrite(LED, HIGH);
  } else {
    digitalWrite(LED, LOW);
  }
  write_debug_output();

}
