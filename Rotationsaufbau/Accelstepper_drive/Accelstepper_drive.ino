// Bounce.pde
// -*- mode: C++ -*-
//
// Make a single stepper bounce from one limit to another
//
// Copyright (C) 2012 Mike McCauley
// $Id: Random.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $

#include <AccelStepper.h>

int drive_speed = 200; // initial speed
int speed_step = 100; // value of speed change 
int runSwitch = 2; // run and stop motor
int upSwitch = 3;  // Push button for increase motor speed
int downSwitch = 4;  // Push button for slow down the motor
int reverseSwitch = 5;  // Push button for reverse
int driverDIR = 8;  
boolean setRun = LOW; // set Motion
boolean setdir = LOW; // Set Direction

// Define a stepper and the pins it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepper(1,7,6);



void start_stop (){
    setRun = !setRun;
    
}

void revmotor (){
  setdir = !setdir;
}

void slower (){
    setRun = 1;
    if (drive_speed > 100){
      drive_speed = drive_speed-speed_step;
    }
    stepper.setSpeed(drive_speed);
}

void faster (){
    setRun = 1;
    if (drive_speed <= (2000-speed_step)){
      drive_speed = drive_speed+speed_step;
    }
    stepper.setSpeed(drive_speed);
}

void setup()
{  
  // Change these to suit your stepper if you want
  pinMode (driverDIR, OUTPUT);
  stepper.setMaxSpeed(2000);
  stepper.setAcceleration(50);
  //stepper.moveTo(2000);
  stepper.setSpeed(drive_speed);
  attachInterrupt(digitalPinToInterrupt(upSwitch), faster, FALLING);
  attachInterrupt(digitalPinToInterrupt(downSwitch), slower, FALLING);
  attachInterrupt(digitalPinToInterrupt(runSwitch), start_stop, FALLING);
  attachInterrupt(digitalPinToInterrupt(reverseSwitch), revmotor, FALLING);
}

void loop()
{
    digitalWrite(driverDIR,setdir);
    if (setRun == 1){
        stepper.runSpeed();
    }
    
}
