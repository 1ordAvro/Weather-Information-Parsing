# Weather Information Parsing

A Python data pipeline that fetches real-time weather data for multiple Indian cities using the OpenWeatherMap API and stores the results in a CSV file.

---

## What It Does

- Fetches live weather data for 5 cities across India via the OpenWeatherMap REST API
- Extracts temperature, weather condition, wind speed, timezone, and location details
- Handles API errors and non-200 responses gracefully
- Appends structured results to a CSV file
- Logs fetch time per city and rate-limits requests to avoid API throttling

---

## Output

Generates `weather_details.csv` with the following columns:

| Column | Description |
|---|---|
| Name | City name returned by API |
| Country | Country code |
| Timezone | UTC offset (e.g. UTC+05:30) |
| Weather | Weather category (e.g. Rain, Clear) |
| Weather Desc. | Detailed description (e.g. light rain) |
| Temp (Deg. C) | Temperature in Celsius |
| Wind Speed (Km/h) | Wind speed |

---

## Tech Stack

- Python 3
- `requests` — HTTP calls to OpenWeatherMap API
- `csv` — writing structured output
- `python-dotenv` — secure API key management via `.env` file

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/1ordAvro/Weather-Information-Parsing.git
cd Weather-Information-Parsing
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install requests python-dotenv
```

**4. Add your API key**

Create a `.env` file in the project root:
```
API_KEY=your_openweathermap_api_key_here
```

Get a free API key at [openweathermap.org](https://openweathermap.org)

**5. Run the pipeline**
```bash
python weather.py
```

---

## Project Structure

```
Weather-Information-Parsing/
│
├── weather.py          # Main pipeline script
├── weather_details.csv # Output file (generated on run)
├── .env                # API key — not tracked in git
├── .gitignore
└── README.md
```

---

## Key Concepts Demonstrated

- REST API consumption with error handling
- Secure credential management using environment variables
- CSV file I/O in Python
- Rate limiting between API calls
- Timezone offset parsing and formatting

---

## Cities Covered

- Barrackpore, West Bengal
- Udaipur, Rajasthan
- Noida, Delhi
- Leh, Ladakh
- Guwahati, Assam
