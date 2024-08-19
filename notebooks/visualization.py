# import the modules 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = 'path_to_your_cleaned_data.csv'  # Update this with the actual path to your cleaned dataset
data = pd.read_csv(file_path)

# 1. Bar Plot of Alerts by Vehicle
plt.figure(figsize=(12, 6))
sns.countplot(x='Vehicle', hue='Alert', data=data)
plt.title('Bar Plot of Alerts by Vehicle')
plt.xlabel('Vehicle')
plt.ylabel('Number of Alerts')
plt.xticks(rotation=45)
plt.show()

# 2. Speed vs. Alerts Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Alert', y='Speed', data=data)
plt.title('Speed Distribution across Different Alerts')
plt.xlabel('Alert Type')
plt.ylabel('Speed (km/h)')
plt.xticks(rotation=45)
plt.show()

# 3. Pair Plot of Numerical Features
sns.pairplot(data[['Speed', 'Lat', 'Long']])
plt.suptitle('Pair Plot of Speed, Latitude, and Longitude', y=1.02)
plt.show()

# 4. Time Series Plot of Alerts Over Days
data['Date'] = pd.to_datetime(data['Date'])
alerts_per_day = data.groupby('Date').size()
plt.figure(figsize=(12, 6))
alerts_per_day.plot()
plt.title('Time Series Plot of Alerts Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Alerts')
plt.show()

# 5. Heatmap of Alerts per Vehicle and Time of Day
data['Hour'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.hour
heatmap_data = data.pivot_table(index='Vehicle', columns='Hour', aggfunc='size', fill_value=0)
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap='coolwarm')
plt.title('Heatmap of Alerts per Vehicle and Time of Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Vehicle')
plt.show()

# Save the figures if needed
plt.savefig('visualization_figures.png')

