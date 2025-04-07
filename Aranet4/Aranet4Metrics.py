import asyncio
import time
from prometheus_client import start_http_server, Gauge
from aranet4 import Aranet4Scanner


SCRAPE_DELAY = 10


def on_scan(advertisement):
    if not advertisement.readings:
        return

    g.set(advertisement.readings.co2)  # Set Prometheus data
    print(advertisement.readings.toString())
    time.sleep(SCRAPE_DELAY)


async def scanAranet4Continuously(argv):
    scanner = Aranet4Scanner(on_scan)
    await scanner.start()
    while True:  # Run forever
        await asyncio.sleep(argv)
    await scanner.stop()


async def scanAranet4():
    scanner = Aranet4Scanner(on_scan)
    await scanner.start()
    await scanner.stop()


# Main process
g = Gauge('CO2_PPM', 'CO2 PPM from Aranet4 Sensor')
# asyncio.run(scanAranet4())  # scans once, so graph doesn't start at 0
print("Starting metrics endpoint")
start_http_server(8000)
try:
    # tell Bleak we are using a graphical user interface that has been properly\
    from bleak.backends.winrt.util import allow_sta
    allow_sta()
    asyncio.run(scanAranet4Continuously(SCRAPE_DELAY))
except KeyboardInterrupt:
    print("User interrupted.")
