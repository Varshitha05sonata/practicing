# Import required libraries
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get today's date and 7 days ago
today = datetime.now()
week_ago = today - timedelta(days=7)

# Convert dates to API format (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Open-Meteo API URL
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude=48.85"
    f"&longitude=2.35"
    f"&start_date={start_date}"
    f"&end_date={end_date}"
    f"&hourly=temperature_2m"
)

# Call the API
# verify=False is used because of your SSL certificate issue
response = requests.get(url, verify=False)

# Check request status
print("Status Code:", response.status_code)

# Convert JSON response to Python dictionary
data = response.json()

# Create DataFrame from hourly weather data
df = pd.DataFrame(data["hourly"])

# Convert time column to datetime format
df["time"] = pd.to_datetime(df["time"])

# Extract only the date part
df["date"] = df["time"].dt.date

# Calculate minimum and maximum temperature for each day
daily_df = df.groupby("date")["temperature_2m"].agg(
    min_temp="min",
    max_temp="max"
).reset_index()

# Print daily temperature data
print(daily_df)

# Create chart
plt.figure(figsize=(10, 6))

# Plot daily maximum temperature
plt.plot(
    daily_df["date"],
    daily_df["max_temp"],
    marker="o",
    label="Maximum Temperature"
)

# Plot daily minimum temperature
plt.plot(
    daily_df["date"],
    daily_df["min_temp"],
    marker="o",
    label="Minimum Temperature"
)

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Paris Daily Minimum and Maximum Temperature")

# Display legend
plt.legend()

# Rotate date labels
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save chart as image
plt.savefig("paris_temperature_chart.png")

# Display chart
plt.show()

if not os.path.exists("data"):  #create empty foleder with data name
    os.makedirs("data")

df.to_csv("data/paris_weather.csv",index=False) #takes the data and convert into csv and saves in data folder
print("Data saved to data/paris_wether.csv")