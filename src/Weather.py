import requests
import csv
import time
import datetime
from pathlib import Path
from Load_env import MY_API_KEY
from Logging import My_logger

class Weather_Details:
    def __init__(self, locations):
        self.locations = locations
        self.logger = My_logger()
        
        self.sl = 0
        self.csv_file = Path("../output/weather_details.csv").absolute()
        self.headers = ["SL.",
                        "Fetched At",
                        "City",
                        "Country",
                        "Timezone",
                        "Weather",
                        "Weather Desc.",
                        "Temp (Deg. C)",
                        "Wind Speed (Km/h)"]
        self.create_storage()

        self.make_request()

    def create_storage(self):
        file_exist = Path(f"{self.csv_file}").is_file()

        if not file_exist:
            with open(self.csv_file, "w") as wd_file:
                csv_writer = csv.DictWriter(wd_file, fieldnames=self.headers, delimiter=",")
                csv_writer.writeheader()
        else:
            with open(self.csv_file, "r") as wd_file:
                rows = list(csv.reader(wd_file))
                if len(rows) > 1:
                    self.sl = int(rows[-1][0])

    def make_request(self):
        for i, loc in enumerate(self.locations, start=self.sl+1):
            payload = {
                "q": loc,
                "appid": MY_API_KEY,
                "units": "metric"
            }

            try:
                r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
            except requests.exceptions.ConnectionError as e:
                self.logger.log_exception(f"Connection failed for {loc}: {e}")
            except requests.exceptions.Timeout as e:
                self.logger.log_exception(f"Request timed out for {loc}: {e}")
            else:
                if r.status_code != 200:
                    self.logger.log_critical(f"{loc} not found")
                    continue
                
                self.logger.log_info(f"Fetched {loc} details in {r.elapsed.total_seconds()} seconds")

                fetched_data = r.json()
                fetched_at = f"{datetime.datetime.now():%Y-%m-%d;%H:%M:%S}"

                city = fetched_data["name"]
                country = fetched_data["sys"]["country"]
                timezone = fetched_data["timezone"]
                hours = timezone // 3600
                minutes = (abs(timezone) % 3600) // 60
                timezone_str = f"UTC{'+' if timezone >= 0 else '-'}{abs(hours):02d}:{minutes:02d}"
                weather_type = fetched_data["weather"][0]["main"]
                weather_desc = fetched_data["weather"][0]["description"]
                temp_in_c = fetched_data["main"]["temp"]
                wind_speed = fetched_data["wind"]["speed"]

                with open(self.csv_file, "a") as wd_file:
                    csv_writer = csv.DictWriter(wd_file, fieldnames=self.headers, delimiter=",")
                    csv_writer.writerow({
                        "SL.": i,
                        "Fetched At": fetched_at,
                        "City": city,
                        "Country": country,
                        "Timezone": timezone_str,
                        "Weather": weather_type,
                        "Weather Desc.": weather_desc,
                        "Temp (Deg. C)": temp_in_c,
                        "Wind Speed (Km/h)": wind_speed
                    })

            time.sleep(0.3)


if __name__ == "__main__":
    locations = ["Barrackpore,WestBengal,India", 
                "Udaipur,Rajasthan,India",
                "Noida,Delhi,India",
                "Leh,Ladakh,India",
                "Guwahati,Assam,India"]
    wd = Weather_Details(locations)