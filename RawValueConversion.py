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








converted_time = pd.DataFrame(data = {'A': ["1"], 'B': ["2"], 'C':["3"]})
time = pd.read_csv(input_file,
                 nrows = 1,
                 header = None,
                 names=['A', 'B', 'C','D','E', 'F', 'G','H','I', 'J', 'K','L','M','N'],
                 sep=",")
if time.at[0,'B'] == 1:
    converted_time.at[0,'A'] = "Sunday"
elif time.at[0,'B'] == 2:
    converted_time.at[0,'A'] = "Monday"
elif time.at[0,'B'] == 3:
    converted_time.at[0,'A'] = "Tuesday"
elif time.at[0,'B'] == 4:
    converted_time.at[0,'A'] = "Wednesday"
elif time.at[0,'B'] == 5:
    converted_time.at[0,'A'] = "Thursday"
elif time.at[0,'B'] == 6:
    converted_time.at[0,'A'] = "Friday"
elif time.at[0,'B'] == 7:
    converted_time.at[0,'A'] = "Saturday"
else:
    print("error converting weekday")
    
converted_time.at[0,'B'] = str(time.at[0,'D'])+"."+str(time.at[0,'F'])+"."+str(time.at[0,'H'])
converted_time.at[0,'C'] = str(time.at[0,'J'])+":"+str(time.at[0,'L'])+":"+str(time.at[0,'N'])
print("starting time of measurement:",converted_time.at[0,'A'],",",converted_time.at[0,'B'],",",converted_time.at[0,'C'])


settings = pd.read_csv(input_file,
                 skiprows = 1,
                 nrows = 1,
                 header = None,
                 names=['A', 'B', 'C','D'],
                 sep=",")
AccelSensitivity = settings.at[0,'A']
GyroSensitivity = settings.at[0,'C']
print("Accelerometer sensitivity set to: ",AccelSensitivity)
print("Gyroscope sensitivity set to: ",GyroSensitivity)



df = pd.read_csv(input_file,
                 skiprows = 2,
                 sep=",")
if AccelSensitivity == 2:
    df[df.columns[0:3]] = df[df.columns[0:3]]/16384
elif AccelSensitivity == 4:
    df[df.columns[0:3]] = df[df.columns[0:3]]/8192
elif AccelSensitivity == 8:
    df[df.columns[0:3]] = df[df.columns[0:3]]/4096
elif AccelSensitivity == 16:
    df[df.columns[0:3]] = df[df.columns[0:3]]/2048

if GyroSensitivity == 250:
    df[df.columns[3:6]] = df[df.columns[3:6]]/131
elif GyroSensitivity == 500:
    df[df.columns[3:6]] = df[df.columns[3:6]]/65.5
elif GyroSensitivity == 1000:
    df[df.columns[3:6]] = df[df.columns[3:6]]/32.8
elif GyroSensitivity == 2000:
    df[df.columns[3:6]] = df[df.columns[3:6]]/16.4

df[df.columns[6:9]] = df[df.columns[6:9]]*0.15


with open(output_file, 'w') as f:
     pd.concat([converted_time], axis=1).to_csv(f,index=False,header=False)
with open(output_file, 'a') as f:
     pd.concat([settings], axis=1).to_csv(f,index=False,header=False)
with open(output_file, 'a') as f:
     pd.concat([df], axis=1).to_csv(f,index=False)

print("Conversion completed.")
