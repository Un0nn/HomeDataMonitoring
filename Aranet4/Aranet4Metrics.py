import asyncio
import time
from prometheus_client import start_http_server, Gauge
import Aranet4Scraping
import os
from dotenv import load_dotenv


load_dotenv()
TARGET_MAC = os.getenv("target_mac")
SCRAPE_DELAY = int(os.getenv("scrape_delay")) if os.getenv("scrape_delay") is not None else 15


print(f"Starting to scan for {TARGET_MAC}")
result = asyncio.run(Aranet4Scraping.get_current_reading(TARGET_MAC))  # scans once, so graph starts at value
g = Gauge('CO2_PPM', 'CO2 PPM from Aranet4 Sensor')
g.set(result.co2)
print("Starting metrics endpoint")
start_http_server(8000)
try:
    print("scanning forever")
    while True:
        result = asyncio.run(Aranet4Scraping.get_current_reading(TARGET_MAC))
        print(f"Found value: {result.co2}")
        g.set(result.co2)
        print(f"Waiting {SCRAPE_DELAY} seconds")
        time.sleep(SCRAPE_DELAY)
except KeyboardInterrupt:
    print("User interrupted.")
