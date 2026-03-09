# Weather Information Parsing

A Python data pipeline that fetches real-time weather data for multiple Indian cities using the OpenWeatherMap API, stores results in a CSV file, and runs automatically on a scheduled interval.

---

## What It Does

- Fetches live weather data for 5 cities across India via the OpenWeatherMap REST API
- Extracts temperature, weather condition, wind speed, and timezone details
- Handles API errors and non-200 responses gracefully with specific exception handling
- Appends structured results to a CSV file with automatic row offset tracking
- Logs pipeline activity to separate files by severity (info, critical, exception)
- Rate-limits requests between API calls to avoid throttling
- Runs automatically every hour via a built-in scheduler

---

## Output

Generates `output/weather_details.csv` with the following columns:

| Column | Description |
|---|---|
| SL. | Auto-incrementing row number, persists across runs |
| Fetched At | Timestamp of when the data was fetched |
| City | City name returned by API |
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
- `csv` — structured output with append and offset logic
- `python-dotenv` — secure API key management via `.env` file
- `logging` — severity-separated log files
- `schedule` — automated pipeline scheduling
- `pathlib` — cross-platform file path handling

---

## Project Structure

```
Weather-Information-Parsing/
│
├── src/
│   ├── Weather.py       # Core pipeline — fetches and stores weather data
│   ├── Scheduler.py     # Entry point — runs pipeline on a schedule
│   ├── Logging.py       # Logger class with severity-separated file handlers
│   └── Load_env.py      # Loads API key from .env file
│
├── output/
│   └── weather_details.csv   # Generated CSV output
│
├── logs/
│   ├── fetched_info.log       # Successful fetch logs
│   ├── fetched_critical.log   # Non-200 API response logs
│   └── fetched_exception.log  # Connection and timeout error logs
│
├── env/
│   └── .env             # API key — not tracked in git
│
├── .gitignore
├── README.md
└── pyproject.toml
```

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
pip install requests python-dotenv schedule
```

**4. Add your API key**

Create a `.env` file inside the `env/` directory:
```
API_KEY=your_openweathermap_api_key_here
```

Get a free API key at [openweathermap.org](https://openweathermap.org)

**5. Run the scheduler**
```bash
cd src
python Scheduler.py
```

The pipeline runs immediately on start, then repeats every hour automatically. Stop it with `Ctrl+C`.

---

## Key Concepts Demonstrated

- REST API consumption with specific exception handling (`ConnectionError`, `Timeout`)
- Secure credential management using environment variables
- CSV file I/O with append logic and persistent row offset across runs
- Structured logging with severity separation across multiple log files
- Handler duplication prevention across repeated instantiations
- OOP design — pipeline logic encapsulated in `Weather_Details` class
- Automated scheduling with `schedule` library
- Proper Python project structure with separated concerns

---

## Cities Covered

- Barrackpore, West Bengal
- Udaipur, Rajasthan
- Noida, Delhi
- Leh, Ladakh
- Guwahati, Assam