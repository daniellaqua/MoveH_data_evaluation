/*
  Stepper Motor Test
  stepper-test01.ino
  Uses MA860H or similar Stepper Driver Unit
  Has speed control & reverse switch
  
  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/
 
// Defin pins
 
//int reverseSwitch = 2;  // Push button for reverse
int upSwitch = 2;  // Push button for increase motor speed
int downSwitch = 3;  // Push button for slow down the motor
int driverPUL = 7;    // PUL- pin
int driverDIR = 6;    // DIR- pin
//int spd = A0;     // Potentiometer
 
// Variables
 
int pd =200;       // Pulse Delay period
boolean setdir = LOW; // Set Direction
 
// Interrupt Handler
 
void revmotor (){
 
  setdir = !setdir;
  
}
 
void down (){
 
  if (pd < 400){
    pd = pd+20;
    }
  
}

void up (){
 
  if (pd > 100){
    pd = pd-20;
  }
}
  
void setup() {
 
  pinMode (driverPUL, OUTPUT);
  pinMode (driverDIR, OUTPUT);
  //attachInterrupt(digitalPinToInterrupt(reverseSwitch), revmotor, FALLING);
  attachInterrupt(digitalPinToInterrupt(upSwitch), up, FALLING);
  attachInterrupt(digitalPinToInterrupt(downSwitch), down, FALLING);
}
 
void loop() {
    // digitalWrite(driverDIR,setdir);
    digitalWrite(driverPUL,HIGH);
    delayMicroseconds(pd);
    digitalWrite(driverPUL,LOW);
    delayMicroseconds(pd);
 
}
