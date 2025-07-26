# Big-Data-Assigment
---------------------
# Uber Fares Data analytical report
### Project Overview & Objectives
This analytical initiative explores Uber fare data to focus on patterns in ride frequency, pricing dynamics, and time based trends. The aim is to transform raw data into actionable insights using Python for data wrangling and Power BI for visualization. Key objectives include:

Differences between peak and off-peak periods

How fare amounts vary by time and distance

When rides occur most frequently

Geographic distribution of pickups

### Methodology: Data collection & analysis approach
The tools I used are: 

- Python (pandas, seaborn, matplotlib): Data cleaning, feature engineering, exploratory data analysis

- Power BI Desktop: Visualizations and dashboard creation

Steps in Python to get data ready:

* Removed missing and duplicate records

* Converted pickup_datetime to datetime format

* Created new features: hour, day, month, weekday, peak_offpeak categorization, distance_km (calculated using latitude/longitude with Haversine formula)

* Saved enhanced dataset to uber_enhanced.csv for use in Power BI

### Analysis: Detailed findings and statistical insights




## 2. Exploratory Data Analysis (EDA)
### A) Descriptive statistics including: Mean, median, mode, standard deviation is in the Python codes I uploaded:
The codes:
```
print(df_clean.describe())
print("Mean fare:", ...)
print("Mode fare:", ...)
```
### B) Visualizations showing fare distribution patterns
<img width="789" height="486" alt="Image" src="https://github.com/user-attachments/assets/d98272f6-3027-44fe-a089-553341b92f33" />

### C) Analyzing relationships between key variables:
### i) Fare amount vs. Distance traveled
<img width="531" height="416" alt="Image" src="https://github.com/user-attachments/assets/e66e9731-b8c1-4b35-aa7f-85d476477807" />

### ii) Fare amount vs. time of day
<img width="536" height="403" alt="Image" src="https://github.com/user-attachments/assets/322a8d7d-03d9-4439-b4e6-d6955173bb0c" />

### iii) Additional relevant correlations
<img width="246" height="199" alt="Image" src="https://github.com/user-attachments/assets/0b648a76-19da-48a3-901b-dc21cdd282da" />

### Correlation Matrix
<img width="744" height="507" alt="Image" src="https://github.com/user-attachments/assets/ecc669c0-5e4c-4f26-baed-d3c346cc1fb3" />

## 4. Data Analysis in Power BI
### Fare patterns across different time intervals & Hourly, daily, and monthly ride patterns
<img width="1336" height="712" alt="Image" src="https://github.com/user-attachments/assets/a35b1ea5-6fd8-4cb8-a6de-eb3695cc2d1b" />

### Seasonal trends and variations

<img width="1346" height="718" alt="Image" src="https://github.com/user-attachments/assets/935b8ae9-f81a-4de4-b22a-883a710ca4f8" />
