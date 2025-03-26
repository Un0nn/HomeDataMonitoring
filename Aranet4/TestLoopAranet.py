import asyncio
import sys

from aranet4 import Aranet4Scanner


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
    print()


async def scanAranet4(argv):
    scanner = Aranet4Scanner(on_scan)
    await scanner.start()
    while True:  # Run forever
        await asyncio.sleep(argv)
    await scanner.stop()


if __name__== "__main__":
    print("starting scanning process")
    scrape_delay = 0
    if len(sys.argv[1:]) == 0:
        scrape_delay = 10  # default to 10
    else:
        scrape_delay = sys.argv[1]
    print(scrape_delay)
    try:
        asyncio.run(scanAranet4(scrape_delay))
    except KeyboardInterrupt:
        print("User interupted.")