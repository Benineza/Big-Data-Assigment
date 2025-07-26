# Big-Data-Assigment
---------------------
# Uber Fares Data analytical report
### Project Overview & Objectives
This analytical initiative explores Uber fare data to focus on patterns in ride frequency, pricing dynamics, and time based trends. The aim is to transform raw data into actionable insights using Python for data wrangling and Power BI for visualization. Key objectives include:

Differences between peak and off peak periods

How fare amounts vary by time and distance

When rides occur most frequently

Geographic distribution of pickups
### Methodology: Data collection & analysis approach
**The tools I used are:**
- Python (pandas, seaborn, matplotlib): Data cleaning, feature engineering, exploratory data analysis
- Power BI Desktop: Visualizations and dashboard creation

**Steps in Python to get data ready:**
* Removed missing and duplicate records
* Converted pickup_datetime to datetime format
* Created new features: hour, day, month, weekday, peak_offpeak categorization, distance_km (calculated using latitude/longitude with Haversine formula)
* Saved enhanced dataset to uber_enhanced.csv for use in Power BI

### Analysis: Detailed findings and statistical insights
**EDA Visualizations:**
* Histogram & Boxplot: Fare distributions showed right-skewed behavior (a few very high fares)
* Correlation matrix: Fare amount is strongly correlated with distance traveled
* Time of Day: Fares tend to spike during peak commute hours (7–10 AM, 4–7 PM)

**Descriptive Statistics:**
+ Mean fare: $11.46
+ Median fare: $8.50
+ Fare range: Mostly $5–$20
+ Outliers: Some rides above $100, indicating long distance trips

**Feature Level Findings:**
* Near linear relationship between fare (fare_amount) and distance (distance_km)
* Higher fares observed during peak times
* Weekends display distinct fare patterns compared to weekdays
### Results: Key discoveries and pattern identification
* Busiest Hours: 7 AM–10 AM and 4 PM–7 PM
* Busiest Weekdays: Friday and Thursday
* Most Rides by Hour: 8 AM and 5 PM
* Most Popular Months: March and April
* Geographic Analysis: Most rides originated from densely populated areas with urban pickup points.
* Fare Distribution:
  * Majority of fares are in the $5–$15 range
  * Outliers suggest premium, long-distance rides or potential data noise
### Conclusion: Summary of main findings
- High value fares are infrequent but significant for revenue
- Fare strongly driven by trip length
- Temporal clustering around commuting hours
- Weekday vs. weekend trends suggest varied trip intent

Power BI provided a dynamic platform to visually explore these trends in real time across dimensions like time, distance, and geography.
### Recommendations: Data driven business suggestions
1. Adjust pricing dynamically: Marginally raise fares during peak periods to maximize earnings without deterring users
2. Smart driver allocation: Focus driver deployment in zones and hours with proven high demand
3. Incentivize off peak usage: Launch promotions during slower times to boost ride volume
4. Bundle long distance rides: Offer special rates or pass systems for long trips to enhance rider retention
5. Targeted regional campaigns: Promote in high  activity urban zones with tailored loyalty and partnership programs
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
