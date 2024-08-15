import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'path_to_your_cleaned_data.csv'  # Update this with the actual path to your cleaned dataset
data = pd.read_csv(file_path)

# 1. Distribution of Alerts
plt.figure(figsize=(10, 6))
sns.countplot(data['Alert'])
plt.title('Distribution of ADAS Alerts')
plt.xlabel('Alert Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Speed Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Speed'], bins=30, kde=True)
plt.title('Speed Distribution at the Time of Alert')
plt.xlabel('Speed (km/h)')
plt.ylabel('Frequency')
plt.show()

# 3. Alerts by Vehicle
plt.figure(figsize=(12, 6))
sns.countplot(y='Vehicle', hue='Alert', data=data)
plt.title('Number of Alerts per Vehicle')
plt.xlabel('Count')
plt.ylabel('Vehicle')
plt.show()

# 4. Alert Frequency by Time of Day
data['Hour'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(data['Hour'], palette='viridis')
plt.title('Alert Frequency by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Alerts')
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Dataset Features')
plt.show()

# 6. Geographical Distribution of Alerts
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Long', y='Lat', hue='Alert', data=data)
plt.title('Geographical Distribution of Alerts')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Save the figures if needed
plt.savefig('eda_figures.png')

