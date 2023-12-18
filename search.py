import numpy as np
import pandas as pd
import re
import json

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('mobile_recommendation_system_dataset.csv')
# Display the first few rows of the DataFrame
print(df.head())

shape = df.shape
# Check for missing values
missing_values = df.isnull().sum()
print(shape, missing_values)

# Remove the rows with missing values
df_clean = df.dropna()
# Check the shape of the cleaned DataFrame
clean_shape = df_clean.shape
# Check for missing values in the cleaned DataFrame
clean_missing_values = df_clean.isnull().sum()
print(clean_shape, clean_missing_values)

def brand_series(name):
    """Extract the series from the name."""
    return name.split('(')[0].strip()

df_clean['name'] = df_clean['name'].apply(brand_series)

unique_name_clean = df_clean['name'].unique()

def create_json():
    list_obj = unique_name_clean.tolist()
    json_string = json.dumps(list_obj)
    return json_string
# print result
print(create_json())