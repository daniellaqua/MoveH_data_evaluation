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
int upSwitch = 3;  // Push button for increase motor speed
int downSwitch = 4;  // Push button for slow down the motor
int runSwitch = 2;
boolean setRun = 0; 


// Define a stepper and the pins it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepper(1,7,6);


void start_stop (){
    setRun = !setRun;
    
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
    if (drive_speed <= (1000-speed_step)){
      drive_speed = drive_speed+speed_step;
    }
    stepper.setSpeed(drive_speed);
}

void setup()
{  
  // Change these to suit your stepper if you want
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(100);
  //stepper.moveTo(2000);
  stepper.setSpeed(drive_speed);
  attachInterrupt(digitalPinToInterrupt(upSwitch), faster, FALLING);
  attachInterrupt(digitalPinToInterrupt(downSwitch), slower, FALLING);
  attachInterrupt(digitalPinToInterrupt(runSwitch), start_stop, FALLING);
}

void loop()
{
    if (setRun == 1){
        stepper.runSpeed();
    }
    
}
