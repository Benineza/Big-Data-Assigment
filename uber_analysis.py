# uber_analysis.py

# 1. Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset
df = pd.read_csv("C:/Users/USER/Desktop/project/uber.csv")
print(df.head())

# 3. Data Overview
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 4. Data Cleaning
df_clean = df.dropna().drop_duplicates().reset_index(drop=True)

# 5. Export cleaned dataset
df_clean.to_csv("uber_cleaned.csv", index=False)

# 6. Feature Engineering
df_clean['Date/Time'] = pd.to_datetime(df_clean['Date/Time'])
df_clean['hour'] = df_clean['Date/Time'].dt.hour
df_clean['day'] = df_clean['Date/Time'].dt.day
df_clean['month'] = df_clean['Date/Time'].dt.month
df_clean['weekday'] = df_clean['Date/Time'].dt.day_name()

def peak_offpeak(hour):
    return 'Peak' if (7 <= hour <= 10 or 16 <= hour <= 19) else 'Off-Peak'

df_clean['peak_offpeak'] = df_clean['hour'].apply(peak_offpeak)

# 7. Export enhanced dataset
df_clean.to_csv("uber_enhanced.csv", index=False)

# 8. Descriptive Statistics
print("Mean fare:", df_clean['fare'].mean())
print("Median fare:", df_clean['fare'].median())
print("Mode fare:", df_clean['fare'].mode()[0])
print("Std deviation:", df_clean['fare'].std())

# 9. Outlier detection (IQR)
Q1 = df_clean['fare'].quantile(0.25)
Q3 = df_clean['fare'].quantile(0.75)
IQR = Q3 - Q1
outliers = df_clean[(df_clean['fare'] < Q1 - 1.5 * IQR) | (df_clean['fare'] > Q3 + 1.5 * IQR)]
print("Number of fare outliers:", len(outliers))

# 11. Correlation
print(df_clean.corr()['fare'])