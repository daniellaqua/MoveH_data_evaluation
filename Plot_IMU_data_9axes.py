# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:11:37 2021

@author: Henrik Domrös, TU Ilmenau


Input: Converted IMU Data as .csv file
Output: Plot 9 axes (Accel,Gyro,Mag)
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read converted CSV (for conversion use RawValueConversion.py)
df = pd.read_csv("C:/Users/Henrik/Desktop/Converted_10.CSV", ",", header=2)


#delete empty spaces in dataframe
df = df.replace(to_replace = np.nan)

#separate columns
xAccel = df["xAccel"]
yAccel = df["yAccel"]
zAccel = df["zAccel"]

xGyro = df["xGyro"]
yGyro = df["yGyro"]
zGyro = df["zGyro"]

xMag = df["xMag"]
yMag = df["yMag"]
zMag = df["zMag"]

plt.rcParams['font.size'] = '16'

fig, axs = plt.subplots(3,1,sharex=True)
axs[0].plot(xAccel, label='x-Accel')
axs[0].plot(yAccel, label='y-Accel')
axs[0].plot(zAccel, label='z-Accel')
axs[0].grid()
axs[0].set_title('Accelerometer', size=20 )
axs[0].set(ylabel ='Acceleration [g-unit]')
axs[0].legend()

axs[1].plot(xGyro, label='x-Gyro')
axs[1].plot(yGyro, label='y-Gyro')
axs[1].plot(zGyro, label='z-Gyro')
axs[1].grid()
axs[1].set_title('Gyroscope', size=20 )
axs[1].set(ylabel ='Rotation [°/s]')
#axs[1].set(xlabel ='Samples' )
axs[1].legend( )

axs[2].plot(xMag, label='x-Mag')
axs[2].plot(yMag, label='y-Mag')
axs[2].plot(zMag, label='z-Mag')
axs[2].grid()
axs[2].set_title('Magnetometer', size=20 )
axs[2].set(ylabel ='Magnetic Field [uT]')
axs[2].set(xlabel ='Samples' )
axs[2].legend( )
