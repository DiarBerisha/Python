import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load and Clean Data
# -----------------------------
df = pd.read_csv("weather_tokyo_data.csv")

# Fix column names (remove spaces)
df.columns = df.columns.str.strip()

# Rename for easier use
df.rename(columns={
    "temperature": "temp",
    "humidity": "humidity",
    "atmospheric pressure": "pressure"
}, inplace=True)

# Clean temperature column (remove parentheses like "(0.3)")
df['temp'] = df['temp'].astype(str).str.replace(r"[()]", "", regex=True)
df['temp'] = pd.to_numeric(df['temp'], errors='coerce')

# Create proper datetime column
df['date'] = pd.to_datetime(df['year'].astype(str) + "/" + df['day'])

# Drop missing values
df = df.dropna(subset=['temp'])

# Extract month
df['month'] = df['date'].dt.month

# -----------------------------
# 2. Temperature Overview
# -----------------------------
avg_temp = df['temp'].mean()
print(f"\nAverage Temperature: {avg_temp:.2f} °C")

# -----------------------------
# 3. Monthly Temperature
# -----------------------------
monthly_avg = df.groupby('month')['temp'].mean()

print("\nMonthly Average Temperatures:")
print(monthly_avg)

# Bar Plot
plt.figure(figsize=(8,5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Highs and Lows
# -----------------------------
hottest_day = df.loc[df['temp'].idxmax()]
coldest_day = df.loc[df['temp'].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)

# -----------------------------
# 5. Temperature Trend
# -----------------------------
df = df.sort_values('date')

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temp'], color='orange')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# -----------------------------
# 6. Seasonal Analysis
# -----------------------------
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['month'].apply(get_season)

seasonal_avg = df.groupby('season')['temp'].mean()

# Order seasons
season_order = ['Winter', 'Spring', 'Summer', 'Fall']
seasonal_avg = seasonal_avg.reindex(season_order)

print("\nSeasonal Average Temperatures:")
print(seasonal_avg)

# Line Plot
plt.figure(figsize=(6,4))
seasonal_avg.plot(marker='o', linestyle='-', color='green')
plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()