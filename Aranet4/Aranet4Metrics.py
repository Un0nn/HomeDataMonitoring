import time
from prometheus_client import start_http_server, Gauge, CollectorRegistry
import Aranet4DataReader
from aranet4 import Aranet4Scanner
import asyncio


SCRAPE_DELAY = 10


def on_scan(advertisement):
    if not advertisement.readings:
        return

    print("=======================================")
    print(f"  Name:             {advertisement.device.name}")
    print(f"  Model:            {advertisement.readings.type.model}")
    print(f"  Address:          {advertisement.device.address}")

    if advertisement.manufacturer_data:
        mf_data = advertisement.manufacturer_data
        print(f"  Version:          {mf_data.version}")
        print(f"  Integrations:     {mf_data.integrations}")
        # print(f"  Disconnected:      {mf_data.disconnected}")
        # print(f"  Calibration state: {mf_data.calibration_state.name}")
        # print(f"  DFU Active:        {mf_data.dfu_active:}")

    print(f"  RSSI:             {advertisement.rssi} dBm")

    if advertisement.readings:
        print("--------------------------------------")
        print(f"  CO2:           {advertisement.readings.co2} pm")
        print(f"  Temperature:   {advertisement.readings.temperature:.01f} \u00b0C")
        print(f"  Humidity:      {advertisement.readings.humidity} %")
        print(f"  Pressure:      {advertisement.readings.pressure:.01f} hPa")
        print(f"  Battery:       {advertisement.readings.battery} %")
        print(f"  Status disp.:  {advertisement.readings.status.name}")
        print(f"  Ago:           {advertisement.readings.ago} s")
        g.set(advertisement.readings.co2)  # Set Prometheus data
    print()


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
asyncio.run(scanAranet4())  # scans once, so graph doesn't start at 0
print("Starting metrics endpoint")
start_http_server(8000)
try:
    # tell Bleak we are using a graphical user interface that has been properly\
    from bleak.backends.winrt.util import allow_sta
    allow_sta()
    asyncio.run(scanAranet4Continuously(SCRAPE_DELAY))
except KeyboardInterrupt:
    print("User interupted.")