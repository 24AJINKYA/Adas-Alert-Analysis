# Sample Data Description.

## Overview
This file provides a summary of the dataset used in the ADAS Alert Analysis project. The dataset consists of approximately 6700 rows, each representing an alert generated by an Advanced Driver Assistance System (ADAS) across different vehicles. Below is a detailed description of the columns present in the dataset and the type of data they contain.

## Columns

1. **Alert**:
   - Description: The type of ADAS alert generated. Alerts include various types that signal different events or conditions encountered by the vehicle.
   - Data Type: Categorical
   - Example Values: "Lane Departure", "Forward Collision Warning", "Pedestrian Detection"

2. **Date**:
   - Description: The date when the alert was triggered.
   - Data Type: Date
   - Format: YYYY-MM-DD
   - Example Values: "2023-07-15", "2023-08-01"

3. **Time**:
   - Description: The exact time the alert was generated.
   - Data Type: Time
   - Format: HH:MM:SS
   - Example Values: "14:30:45", "08:15:30"

4. **Lat (Latitude)**:
   - Description: The latitude of the vehicle's location when the alert was triggered.
   - Data Type: Float
   - Example Values: 28.7041, 12.9716

5. **Long (Longitude)**:
   - Description: The longitude of the vehicle's location when the alert was triggered.
   - Data Type: Float
   - Example Values: 77.1025, 77.5946

6. **Vehicle**:
   - Description: Identifier for the vehicle that generated the alert. There are 5 different vehicles in the dataset.
   - Data Type: Categorical
   - Example Values: "Vehicle_1", "Vehicle_2", "Vehicle_3"

7. **Speed**:
   - Description: The speed of the vehicle at the time the alert was generated, measured in kilometers per hour (km/h).
   - Data Type: Float
   - Example Values: 45.5, 70.2
  
![image](https://github.com/user-attachments/assets/6ef3d553-1257-42ec-b167-f8e6a5693b02)


## Additional Information
- **Total Rows**: Approximately 6700 rows
- **Purpose**: The dataset is used to analyze the occurrence of various ADAS alerts and their relationship with vehicle speed and location. This analysis aims to identify patterns and potential risk factors in different driving conditions.

## Notes
- The latitude and longitude values can be used to map the exact location where each alert was triggered.
- Vehicle speeds are critical in determining how driving behavior influences the frequency and type of alerts generated.

