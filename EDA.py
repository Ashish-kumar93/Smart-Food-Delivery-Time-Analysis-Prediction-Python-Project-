# =========================================================
# OBJECTIVE 1:
# Data Cleaning, Preprocessing and EDA
# =========================================================

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("projectpython.csv")

# -------------------- BASIC EDA --------------------
print("\nDATA INFO")
df.info()

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

print("\nFIRST 5 ROWS")
print(df.head())

# -------------------- CLEANING --------------------

# Strip column names
df.columns = df.columns.str.strip()

# Fix Time_taken column
df['Time_taken(min)'] = df['Time_taken(min)'].astype(str)
df['Time_taken(min)'] = df['Time_taken(min)'].str.replace('(min) ', '', regex=False)
df['Time_taken(min)'] = df['Time_taken(min)'].astype(float)

# Clean Weather column
df['Weatherconditions'] = df['Weatherconditions'].str.replace('conditions ', '', regex=False)

# -------------------- HANDLE MISSING VALUES --------------------

# Numerical columns-median
num_cols = df.select_dtypes(include=['int64','float64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns-mode
cat_cols = df.select_dtypes(include=['object', 'string']).columns
for col in cat_cols:
    if df[col].mode().empty:
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# -------------------- DUPLICATES --------------------
print("\nDUPLICATE VALUES:", df.duplicated().sum())
df = df.drop_duplicates()

#FEATURE ENGINEERING 


#Distance calculation using Haversine formula

from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

df['Distance'] = df.apply(lambda x: haversine(
    x['Restaurant_latitude'], x['Restaurant_longitude'],
    x['Delivery_location_latitude'], x['Delivery_location_longitude']
), axis=1)

# -----OUTLIER REMOVAL ------
Q1 = df['Time_taken(min)'].quantile(0.25)
Q3 = df['Time_taken(min)'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Time_taken(min)'] >= Q1 - 1.5*IQR) & 
        (df['Time_taken(min)'] <= Q3 + 1.5*IQR)]

print("\nFINAL DATA SHAPE:", df.shape)

#----- FINAL CHECK ----
print("\nFINAL DATA TYPES")
print(df.dtypes)
