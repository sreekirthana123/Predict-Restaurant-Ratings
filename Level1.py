import pandas as pd
import numpy as np

# ============================================
# CONFIGURATION - UPDATE YOUR FILE PATH HERE
# ============================================

# METHOD 1: Use forward slashes (RECOMMENDED - EASIEST)
FILE_PATH = "C:/Users/Sree Kirthana/Documents/Data Engineering/Railway_info.csv"

# METHOD 2: Use raw string (put 'r' before the quotes)
# FILE_PATH = r"C:\Users\Sree Kirthana\Documents\Data Engineering\Railway_info.csv"

# METHOD 3: Use double backslashes
# FILE_PATH = "C:\\Users\\Sree Kirthana\\Documents\\Data Engineering\\Railway_info.csv"

# Choose any ONE method above and update with your actual file path
# ============================================

# Task 1.1: Load and Inspect Data
print("=" * 60)
print("TASK 1.1: LOAD AND INSPECT DATA")
print("=" * 60)

# Load the dataset with multiple encoding attempts
print(f"\nLoading data from: {FILE_PATH}")

encodings_to_try = ['latin-1', 'iso-8859-1', 'cp1252', 'utf-8', 'utf-8-sig', 'windows-1252']
df = None

for encoding in encodings_to_try:
    try:
        print(f"Trying encoding: {encoding}...", end=" ")
        df = pd.read_csv(FILE_PATH, encoding=encoding, encoding_errors='ignore')
        print(f"✓ SUCCESS!")
        break
    except Exception as e:
        print(f"✗ Failed")
        continue

if df is None:
    print("\n✗ ERROR: Could not load file with any encoding.")
    print("Trying one more time with error handling...")
    try:
        df = pd.read_csv(FILE_PATH, encoding='latin-1', errors='ignore')
        print("✓ Loaded with error handling (some characters may be skipped)")
    except Exception as e:
        print(f"✗ CRITICAL ERROR: {str(e)}")
        print("Please check your file path and ensure the file is not corrupted.")
        exit()

# Display first 10 rows
print("\nFirst 10 rows of the dataset:")
print(df.head(10))

# Display basic structure
print("\n\nDataset Shape (rows, columns):")
print(f"{df.shape[0]} rows and {df.shape[1]} columns")

print("\n\nColumn Names and Data Types:")
print(df.dtypes)

print("\n\nDataset Information:")
print(df.info())

print("\n\nMissing Values Count:")
print(df.isnull().sum())

print("\n\nMissing Values Percentage:")
print((df.isnull().sum() / len(df) * 100).round(2))


# Task 1.2: Basic Statistics
print("\n\n" + "=" * 60)
print("TASK 1.2: BASIC STATISTICS")
print("=" * 60)

# Total number of trains
total_trains = df.shape[0]
print(f"\nTotal number of trains: {total_trains}")

# Unique source stations
unique_sources = df['Source_Station_Name'].nunique()
print(f"Number of unique source stations: {unique_sources}")

# Unique destination stations
unique_destinations = df['Destination_Station_Name'].nunique()
print(f"Number of unique destination stations: {unique_destinations}")

# Most common source station
most_common_source = df['Source_Station_Name'].mode()[0]
source_count = df['Source_Station_Name'].value_counts().iloc[0]
print(f"\nMost common source station: {most_common_source}")
print(f"Number of trains from {most_common_source}: {source_count}")

# Most common destination station
most_common_destination = df['Destination_Station_Name'].mode()[0]
dest_count = df['Destination_Station_Name'].value_counts().iloc[0]
print(f"\nMost common destination station: {most_common_destination}")
print(f"Number of trains to {most_common_destination}: {dest_count}")

# Display top 5 source stations
print("\n\nTop 5 Source Stations:")
print(df['Source_Station_Name'].value_counts().head())

# Display top 5 destination stations
print("\n\nTop 5 Destination Stations:")
print(df['Destination_Station_Name'].value_counts().head())


# Task 1.3: Data Cleaning
print("\n\n" + "=" * 60)
print("TASK 1.3: DATA CLEANING")
print("=" * 60)

# Create a copy for cleaning
df_cleaned = df.copy()

# Handle missing values
print("\nHandling Missing Values:")
print("Before cleaning:")
print(df_cleaned.isnull().sum())

# Strategy for handling missing values (you can adjust based on your data)
# Option 1: Drop rows with missing values
# df_cleaned = df_cleaned.dropna()

# Option 2: Fill missing values with appropriate values
for col in df_cleaned.columns:
    if df_cleaned[col].isnull().any():
        if df_cleaned[col].dtype == 'object':
            # Fill text columns with 'Unknown'
            df_cleaned[col].fillna('Unknown', inplace=True)
        else:
            # Fill numeric columns with median
            df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)

print("\nAfter cleaning:")
print(df_cleaned.isnull().sum())

# Standardize station names to uppercase
print("\n\nStandardizing Station Names to Uppercase:")
print("Sample before standardization:")
print(df_cleaned[['Source_Station_Name', 'Destination_Station_Name']].head(3))

df_cleaned['Source_Station_Name'] = df_cleaned['Source_Station_Name'].str.upper().str.strip()
df_cleaned['Destination_Station_Name'] = df_cleaned['Destination_Station_Name'].str.upper().str.strip()

print("\nSample after standardization:")
print(df_cleaned[['Source_Station_Name', 'Destination_Station_Name']].head(3))

# Save cleaned data
df_cleaned.to_csv('train_data_cleaned.csv', index=False)
print("\n\nCleaned data saved as 'train_data_cleaned.csv'")

# Summary statistics
print("\n\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Original dataset: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Cleaned dataset: {df_cleaned.shape[0]} rows, {df_cleaned.shape[1]} columns")
print(f"Rows removed: {df.shape[0] - df_cleaned.shape[0]}")
print("\nLevel 1 tasks completed successfully!")