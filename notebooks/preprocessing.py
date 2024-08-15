# ADAS Alert Data Preprocessing
# This notebook will guide you through the preprocessing steps for the ADAS Alert Analysis project.
# We will load the dataset, explore its structure, and perform basic data cleaning and preprocessing.

# Import necessary libraries
import pandas as pd

# Load the dataset
file_path = 'path_to_your_csv_file.csv'  # Update this with the actual path to your dataset
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head()

# Basic Information about the dataset
print("Dataset Information:")
data.info()

# Check for any missing values in the dataset
print("\nMissing Values in the Dataset:")
print(data.isnull().sum())

# Drop rows with any missing values
data = data.dropna()

# Display the number of rows and columns after removing missing values
print(f"\nDataset Shape after removing missing values: {data.shape}")

# Get the list of unique vehicles in the dataset
unique_vehicles = data['Vehicle'].unique()
print(f"\nNumber of unique vehicles: {len(unique_vehicles)}")
print("Vehicle identifiers:", unique_vehicles)

# Get the list of unique alerts in the dataset
unique_alerts = data['Alert'].unique()
print(f"\nNumber of unique alert types: {len(unique_alerts)}")
print("Alert types:", unique_alerts)

# Convert the 'Date' and 'Time' columns to datetime format for easier analysis
data['Date'] = pd.to_datetime(data['Date'])
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.time

# Extract year, month, and day from the 'Date' column for further analysis
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Display the first few rows of the updated dataset to confirm the changes
data.head()

# Checking for duplicate rows
duplicates = data.duplicated()
print(f"\nNumber of duplicate rows in the dataset: {duplicates.sum()}")

# Remove duplicate rows
data = data.drop_duplicates()

# Display the dataset shape after removing duplicates
print(f"\nDataset Shape after removing duplicates: {data.shape}")

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_data.csv'  # Update this with the desired path for the cleaned data
data.to_csv(cleaned_file_path, index=False)

print("\nPreprocessing complete. Cleaned data saved to:", cleaned_file_path)
