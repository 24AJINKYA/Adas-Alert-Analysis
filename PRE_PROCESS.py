# PREPROCESSING
import pandas as pd

# Load the Excel file
file_path = "data.csv" # Replace with your file path
data = pd.read_csv(file_path)

# Display the first few rows to verify the data
print(data.head())

            
                     Alert        Date      Time        Lat       Long  Vehicle  Speed  Unnamed: 7  Unnamed: 8  Unnamed: 9
            0  cas_fcw  01-06-2022  06:26:32  12.724588  79.982251      805     33         NaN         NaN         NaN
            1  cas_fcw  01-06-2022  06:41:35  12.630791  79.931575      805     58         NaN         NaN         NaN
            2  cas_fcw  01-06-2022  17:01:28  12.747127  79.995694      805     58         NaN         NaN         NaN
            3  cas_fcw  01-06-2022  17:46:32  12.528537  79.898806      805     59         NaN         NaN         NaN
            4  cas_hmw  01-06-2022  06:14:53  12.815835  80.033858      805     45         NaN         NaN         NaN




### CHECKING FOR NULL VALUES 

missing_values = data.isnull().sum()
print(missing_values)


                                    Alert            0
                                    Date             0
                                    Time             0
                                    Lat              0
                                    Long             0
                                    Vehicle          0
                                    Speed            0


# Analysing the Number of alerts in the DAta 


                        
alert_counts = data['Alert'].value_counts()
print(alert_counts)


                        cas_hmw    4054
                        cas_ldw    2052
                        cas_pcw     438
                        cas_fcw     158
                        Name: Alert, dtype: int64



##Removing Duplicated 


                        
 data_cleaned = data.drop_duplicates()



## aNALYSIS OF ALERTS AND wARNINGS oOCCURANCE 

             import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.countplot(data=data, x='Alert')
plt.title('Distribution of ADAS Alerts')
plt.show()



             screen shot######################################

### DEPENDING ON SPEED ALERTS 
# Ensure the 'Speed' column is numeric
data['Speed'] = pd.to_numeric(data['Speed'], errors='coerce')

# Remove any rows with missing speed or alert values
data = data.dropna(subset=['Speed', 'Alert'])

# Step 1: Aggregate Alerts by Speed
alerts_by_speed = data.groupby(['Speed', 'Alert']).size().unstack().fillna(0)

# Step 2: Visualize the Relationship
plt.figure(figsize=(12, 8))

# Plotting each alert type with respect to speed
for alert_type in alerts_by_speed.columns:
    sns.lineplot(x=alerts_by_speed.index, y=alerts_by_speed[alert_type], label=alert_type)

plt.title('Frequency of Alerts Occurring at Different Speeds')
plt.xlabel('Speed')
plt.ylabel('Number of Alerts')
plt.legend(title='Alert Type')
plt.grid(True)
plt.show()


######################## SCREEN SHOT #####################################



               


                        
