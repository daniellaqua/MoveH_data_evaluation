# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:25:22 2020

@author: Max Kogel, TU Ilmenau

Input: raw sensor data as .csv file
Output: Converted data as .csv file
    Accelerometer values in g-unit
    Gyroscope values in degrees per second

Accel Sensitivity Mode:
    2g  - raw Value / 16384
    4g  - raw Value / 8192
    8g  - raw Value / 4096
    16g - raw Value / 2048
Gyro Sensitivity Mode:
    250dps  - raw Value / 131
    500dps  - raw Value / 65.5
    1000dps - raw Value / 32.8
    2000dps - raw Value / 16.4

"""

import pandas as pd


"""
Change input_file to the path of your raw data file
Change output_file to desired path for converted .csv file

"""
input_file = r"C:\Users\MaxKo\Desktop\RAW_00.CSV"
output_file = r"C:\Users\MaxKo\Desktop\ConvertedMotionValues_00.CSV"







settings = pd.read_csv(input_file,
                 nrows = 1,
                 sep=",")

AccelSensitivity = settings.columns[0]
GyroSensitivity = settings. columns[2]
print("Accelerometer sensitivity set to: ",AccelSensitivity)
print("Gyroscope Sensitivity set to: ",GyroSensitivity)

df = pd.read_csv(input_file,
                 skiprows = 1,
                 sep=",")

if AccelSensitivity == '2':
    df[df.columns[0:3]] = df[df.columns[0:3]]/16384
elif AccelSensitivity == '4':
    df[df.columns[0:3]] = df[df.columns[0:3]]/8192
elif AccelSensitivity == '8':
    df[df.columns[0:3]] = df[df.columns[0:3]]/4096
elif AccelSensitivity == '16':
    df[df.columns[0:3]] = df[df.columns[0:3]]/2048

if GyroSensitivity == '250':
    df[df.columns[3:6]] = df[df.columns[3:6]]/131
elif GyroSensitivity == '500':
    df[df.columns[3:6]] = df[df.columns[3:6]]/65.5
elif GyroSensitivity == '1000':
    df[df.columns[3:6]] = df[df.columns[3:6]]/32.8
elif GyroSensitivity == '2000':
    df[df.columns[3:6]] = df[df.columns[3:6]]/16.4

df[df.columns[6:9]] = df[df.columns[6:9]]*0.15
df.to_csv(output_file, sep=",")

print("Conversion completed.")
