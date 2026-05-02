import pandas as pd
import matplotlib as plt


df = pd.read_csv("weather_tokyo_data.csv")


df.columns = df.columns.str.strip()

df.rename(columns={
    "temperature": "temp",
    "humidity": "humidity",
    "atmospheric pressure": "pressure"
}, inplace=True)


df['temp'] = df['temp'].astype(str).str.replace(r"[()]", "", regex=True)
df['temp'] = pd.to_numeric(df['temp'], errors='coerce')


df['date'] = pd.to_datetime(df['year'].astype(str) + "/" + df['day'])

df = df.dropna(subset=['temp'])


df['month'] = df['date'].dt.month


