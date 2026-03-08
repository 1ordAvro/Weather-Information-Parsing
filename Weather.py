import os
from dotenv import load_dotenv
import requests
import csv
import time

load_dotenv()

MY_KEY = os.getenv("API_KEY")
headers = ["Name", "Country", "Timezone", "Weather", "Weather Desc.", "Temp (Deg. C)", "Wind Speed (Km/h)"]
locations = ["Barrackpore,WestBengal,India", "Udaipur,Rajasthan,India", "Noida,Delhi,India", "Leh,Ladakh,India", "Guwahati,Assam,India"]

with open("weather_details.csv", "w") as wd_file:
    csv_writer = csv.DictWriter(wd_file, fieldnames=headers, delimiter=",")
    csv_writer.writeheader()

for loc in locations:
    payload = {
        "q": loc,
        "APPID": MY_KEY,
        "units": "metric"
    }

    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
    except requests.exceptions.ConnectionError as e:
        print(f"Connection failed for {loc}: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Request timed out for {loc}: {e}")
    else:
        if r.status_code != 200:
            print(f"There is an issue fetching weather details of {loc}...")
            continue

        print(f"Fetched {loc} details in {r.elapsed.total_seconds()} seconds...")

        fetched_data = r.json()

        name = fetched_data["name"]
        country = fetched_data["sys"]["country"]
        timezone = fetched_data["timezone"]
        hours = timezone // 3600
        minutes = (abs(timezone) % 3600) // 60
        timezone_str = f"UTC{'+' if timezone >= 0 else '-'}{abs(hours):02d}:{minutes:02d}"
        weather_type = fetched_data["weather"][0]["main"]
        weather_desc = fetched_data["weather"][0]["description"]
        temp_in_c = fetched_data["main"]["temp"]
        wind_speed = fetched_data["wind"]["speed"]

        with open("weather_details.csv", "a") as wd_file:
            csv_writer = csv.DictWriter(wd_file, fieldnames=headers, delimiter=",")
            csv_writer.writerow({
                "Name": name,
                "Country": country,
                "Timezone": timezone_str,
                "Weather": weather_type,
                "Weather Desc.": weather_desc,
                "Temp (Deg. C)": temp_in_c,
                "Wind Speed (Km/h)": wind_speed
            })

    time.sleep(0.3)