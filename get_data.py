import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min&timezone=auto&start_date={start_date}&end_date={end_date}"

response = requests.get(url)
data = response.json()
print(data)

daily_data = data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

df['date'] = pd.to_datetime(df['date'])

print(df)

plt.plot(df['date'], df['max_temp'], label='Max Temp')
plt.plot(df['date'], df['min_temp'], label='Min Temp')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature over the last week')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('weather_chart.png')
plt.show()

if not os.path.exists('data'):
       os.makedirs('data')

df.to_csv('data/weather_data.csv', index=False)
print("Data saved to data/weather_data.csv")      