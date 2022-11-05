
/*obstacle avoiding,bluetooth control,voice control robot car.
   
*/
#include <Servo.h>
#include <AFMotor.h>

#define Echo A0
#define Trig A1
#define motor 10
#define Speed 170
#define spoint 103

char value;
int distance;
int Left;
int Right;
int L = 0;
int R = 0;
int L1 = 0;
int R1 = 0;
int info = 0;//variable for the information comming from the bluetooth module
int state = 0;//simple variable for displaying the state
int LED;

Servo servo;
AF_DCMotor M1(1);
AF_DCMotor M2(2);
AF_DCMotor M3(3);
AF_DCMotor M4(4);

void setup() {
  Serial.begin(9600);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
  pinMode(13, OUTPUT);
  servo.attach(motor);
  M1.setSpeed(Speed);
  M2.setSpeed(Speed);
  M3.setSpeed(Speed);
  M4.setSpeed(Speed);
  Serial.println("CLEARDATA");
  Serial.println("LABEL,CLOCK,CM");
  
  
}
void loop() {
  Obstacle();
  //Mobilecontrol();
  Bluetoothcontrol();
  
}

void Bluetoothcontrol(){

  if(Serial.available() > 0){  //if there is any information comming from the serial lines...
    info = Serial.read();   
    state = 0;   //...than store it into the "info" variable
  }
  if(info == '1'){                //if it gets the number 1(stored in the info variable...
    digitalWrite(LED, HIGH);    //it's gonna turn the led on(the on board one)
    if(state == 0){              //if the flag is 0, than display that the LED is on and than set that value to 1
      Serial.println("LED ON");  //^^that will prevent the arduino sending words LED ON all the time, only when you change the state
      state = 1;
    }
   }
  else if(info == '0'){
    digitalWrite(LED, LOW);      //else, it's going to turn it off
    if(state == 0){
      Serial.println("LED OFF");//display that the LED is off
      state = 1;
     }
  }
}
  
void Obstacle() {
  distance = ultrasonic();
  if (distance <= 15) {
    Stop();
    backward();
    delay(100);
    Stop();
    L = leftsee();
    servo.write(spoint);
    delay(800);
    R = rightsee();
    servo.write(spoint);
    if (L < R) {
      right();
      delay(500);
      Stop();
      delay(200);
    } else if (L > R) {
      left();
      delay(500);
      Stop();
      delay(200);
    }
  } else {
    forward();
  }

}

void Mobilecontrol() {
  distance = ultrasonic();
  if (Serial.available() > 0) {
    value = Serial.read();
    Serial.println(value);
  }
  if (value == 'F') {
    forward();
  } else if (value == 'B') {
    backward();
  } else if (value == 'L') {
    left();
  } else if (value == 'R') {
    right();
  } else if (value == 'S') {
    Stop();
  }
}



int ultrasonic() {
  digitalWrite(Trig, LOW);
  delayMicroseconds(4);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  int t = pulseIn(Echo, HIGH);
  int cm = (t/2) / 29.1;//time convert distance
  if (cm<15){
    Serial.print(cm);
    Serial.print("cm");
    Serial.print(" ALERT");
    }
  else{
    Serial.print(cm);//printing the numbers
    Serial.print("cm");//and the unit
  }
         
  Serial.println(" ");
  return cm;

  
  if(distance <= 15){  //if we get too close, the LED will turn off, that's the method with my RC car, if it gets too close, it turns off, but that will be in the next instructable :)
    digitalWrite(LED, LOW);
    Serial.println("TOO CLOSE!!!");
    delay(2000); //so the stopping is visabl
  }
  
}

void forward() {
  M1.run(FORWARD);
  M2.run(FORWARD);
  M3.run(FORWARD);
  M4.run(FORWARD);
}
void backward() {
  M1.run(BACKWARD);
  M2.run(BACKWARD);
  M3.run(BACKWARD);
  M4.run(BACKWARD);
}
void right() {
  M1.run(BACKWARD);
  M2.run(BACKWARD);
  M3.run(FORWARD);
  M4.run(FORWARD);
}
void left() {
  M1.run(FORWARD);
  M2.run(FORWARD);
  M3.run(BACKWARD);
  M4.run(BACKWARD);
}
void Stop() {
  M1.run(RELEASE);
  M2.run(RELEASE);
  M3.run(RELEASE);
  M4.run(RELEASE);
}
int rightsee() {
  servo.write(20);
  delay(800);
  Left = ultrasonic();
  return Left;
}

int leftsee() {
  servo.write(180);
  delay(800);
  Right = ultrasonic();
  return Right;
}
