import numpy as np
import pandas as pd
import re
import json
import sys
from statistics import mean
from sklearn.metrics.pairwise import cosine_similarity

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



def extract_storage(corpus):
    """Extract the storage capacity from the corpus."""
    match = re.search(r'Storage(\d+)', corpus)
    if match:
        return int(match.group(1))
    return None

def extract_ram(corpus):
    """Extract the RAM from the corpus."""
    match = re.search(r'RAM(\d+)', corpus)
    if match:
        return int(match.group(1))
    return None

def extract_system(corpus):
    """Extract the operating system from the corpus."""
    match = re.search(r'System(.*?)Processor', corpus)
    if match:
        return match.group(1).strip()
    return None

def extract_processor(corpus):
    """Extract the processor type from the corpus."""
    match = re.search(r'Processor (.*?) ', corpus)
    if match:
        return match.group(1).strip()
    return None

def extract_brand(name):
    """Extract the brand from the name."""
    return name.split()[0]

def brand_series(name):
    """Extract the series from the name."""
    return name.split('(')[0].strip()

def clean_system(system):
    """Clean the system values."""
    if pd.isnull(system):
        return None
    if 'android' in system.lower():
        return 'Android'
    if 'ios' in system.lower():
        return 'iOS'
    if 'tizen' in system.lower():
        return 'Tizen'
    return system

def clean_processor(processor):
    """Clean the processor values."""
    if pd.isnull(processor):
        return None
    if 'mediatek' in processor.lower():
        return 'MediaTek'
    if 'qualcomm' in processor.lower():
        return 'Qualcomm'
    if 'apple' in processor.lower():
        return 'Apple'
    return 'Other'

def clean_price(price):
    """Clean the price values."""
    # Remove any non-numeric characters
    cleaned_price = re.sub(r'\D', '', price)

    # Convert the remaining value to an integer
    try:
        return int(cleaned_price)
    except ValueError:
        return None

# Apply the function to the 'corpus' column
df_clean['Storage'] = df_clean['corpus'].apply(extract_storage)
df_clean['RAM'] = df_clean['corpus'].apply(extract_ram)
df_clean['System'] = df_clean['corpus'].apply(extract_system)
df_clean['Processor'] = df_clean['corpus'].apply(extract_processor)

unique_systems = df_clean['System'].unique()
unique_processors = df_clean['Processor'].unique()
print(unique_systems, unique_processors)

df_clean['System'] = df_clean['System'].apply(clean_system)

# # Check the unique values for 'System'
# unique_systems_clean = df_clean['System'].unique()

# print(unique_systems_clean)

df_clean['Processor'] = df_clean['Processor'].apply(clean_processor)

# # Check the unique values for 'Processor'
# unique_processors_clean = df_clean['Processor'].unique()

# print(unique_processors_clean)

# Apply the function to the 'price' column
df_clean['price'] = df_clean['price'].apply(clean_price)

# Handling Outliers
print("Deteksi Outlier")
outliers=[]
def detect_outlier(data):
    threshold=3
    mean = np.mean(data)
    std = np.std(data)
    for x in data:
        z_score = (x - mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(x)
    return outliers

outlier1 = detect_outlier(df_clean['price'])
print("outlier kolom Price : ", outlier1)
print("outlier kolom Price : ", len(outlier1))
print()


variabel = ['price']
for var in variabel:
    outlier_datapoints = detect_outlier(df_clean[var])
    print("Outlier ", var, " = ", outlier_datapoints)
    rata = mean(df_clean[var])
    print("Outlier ", var, "telah diganti menjadi mean : ")
    df_clean[var] = df_clean[var].replace(outlier_datapoints, rata)
    print(df_clean)


print("data setelah hapus missing value dan handling outlier")
print(df_clean.head())


# Check the first few rows of the DataFrame
# print(df_clean.head())

# Apply the function to the 'name' column
df_clean['Brand'] = df_clean['name'].apply(extract_brand)

df_clean['name'] = df_clean['name'].apply(brand_series)
# Check the unique values for 'System'
# Get unique values
unique_name_clean = df_clean['name'].unique()

# Remove rows based on unique values
df_clean = df_clean.sort_values(by='price', ascending=False)
df_clean = df_clean.drop_duplicates(subset='name')
print(df_clean)


iphone_ram_mapping = {
    'iPhone 14': 6,
    'iPhone 13': 4,
    'iPhone 13 Pro': 6,
    'iPhone 12': 4,
    'iPhone 12 Pro': 6,
    'iPhone 11': 4,
    'iPhone X': 3,
    'iPhone XR': 3,
    'iPhone XS': 4,
    'iPhone 8': 2,
    'iPhone 8 Plus': 3,
    'iPhone 7': 2,
    'iPhone 7 Plus': 3,
    'iPhone 6': 1,
    'iPhone 6S': 2,
    'iPhone 5': 1,
    'iPhone SE': 2,
    'iPhone SE 3rd Gen': 4,
    'IPhone 4': .512
}

for model_name, ram_value in iphone_ram_mapping.items():
    df_clean.loc[df_clean.name.str.contains(model_name, case = True), 'RAM'] = ram_value

other_phones_ram_mapping = {
    'OPPO Reno10 5G': 8,
    'SAMSUNG Guru Music 2': 0.008,
    'SAMSUNG GT-E1215ZWAINS': 0,
    'Infinix Smart 7 HD': 2,
    'SAMSUNG Galaxy A2 Core': 1,
    'SAMSUNG Guru FM Plus': 0.004,
    'SAMSUNG Galaxy A13': 4,
    'SAMSUNG Metro 313': 0.016
}

for model_name, ram_value in other_phones_ram_mapping.items():
    df_clean.loc[df_clean.name.str.contains(model_name, case = True), 'RAM'] = ram_value

phone_processor_mapping = {
    'Xiaomi': 'Qualcomm',
    'REDMI': 'MediaTek',
    'Tecno': 'MediaTek',
    'OPPO': 'Qualcomm',
    'OnePlus': 'MediaTek',
    'SAMSUNG': 'Other',
    'IPhone 4': 'Other',
    'MOTOROLA': 'Qualcomm',
    'vivo Z1x': 'Qualcomm',
    'realme': 'MediaTek',
    'a 10e': 'Other',
    'A10E': 'Other',
    'Peace': 'Other'
}

for model_name, processor_name in phone_processor_mapping.items():
    condition = (df_clean.name.str.contains(model_name, case=True)) & (pd.isna(df_clean['Processor']))
    df_clean.loc[condition, 'Processor'] = processor_name

missing_storage_mapping = {
    'SAMSUNG Guru Music 2': 16,
    'SAMSUNG GT-E1215ZWAINS': 0,
    'SAMSUNG Galaxy A2 Core': 16,
    'SAMSUNG Guru FM Plus': 0,
    'SAMSUNG Galaxy A13': 64,
}

for model_name, storage_value in missing_storage_mapping.items():
    df_clean.loc[df_clean.name.str.contains(model_name, case = True), 'Storage'] = storage_value

print(df_clean.columns)
del df_clean['corpus']
desired_order = ['name', 'ratings', 'price', 'Storage', 'RAM', 'Processor', 'Brand', 'System', 'imgURL']
df_clean = df_clean.reindex(columns=desired_order)
print(df_clean.columns)
# Check the first few rows of the DataFrame
print(df_clean.head())

def recommend_devices(latest_phone):
    """Recommend devices based on user preferences."""
    df_filtered = df_clean[
        (df_clean['name'] == latest_phone)
    ]

    if not df_filtered.empty:
        user_vector = df_filtered.iloc[:, 2:5]
        similarities = cosine_similarity(user_vector, df_clean.iloc[:, 2:5])[0]
        df_result = df_clean.copy()
        df_result = df_result.reset_index(drop=True)
        for i in range(len(df_result)):
            df_result.loc[i, 'similarity'] = similarities[i]

        df_result = df_result[df_result['name'] != latest_phone]
        recommendations = df_result.iloc[similarities.argsort()[::-1][:8]]
        recommendations = recommendations.sort_values('similarity', ascending=False)
    else:
        recommendations = df_filtered

    json_string = recommendations.to_json()
    # print result
    return json_string

print('')
inputphone = sys.argv[1]
print(recommend_devices(latest_phone=inputphone))