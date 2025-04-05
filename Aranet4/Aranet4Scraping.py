import asyncio
import time
from aranet4.client import Aranet4Advertisement
from bleak import BleakScanner


async def scan_aranet4_device(aranet4_mac: str, scrape_interval: int):
    """
    Scans aranet device, waiting scrape_interval seconds between scans
    scrape_interval is only the wait time, so expect the time between data to be a couple seconds longer than scrape_interval
    """
    stop_event = None

    # callback for scanner
    def callback(device, ad_data):
        # if device address matches aranet address, set stop_event, that will stop scanner.
        if device.address == aranet4_mac:
            adv = Aranet4Advertisement(device, ad_data)
            print("Found specified Aranet4.")
            if adv:
                print(adv.readings.toString())
            stop_event.set()

    while True:
        stop_event = asyncio.Event()
        async with BleakScanner(callback):
            print("Scanner started")

            # wait for correct device in callback
            await stop_event.wait()
            print("Scanner stopped.")

        time.sleep(scrape_interval)


asyncio.run(scan_aranet4_device("60:C0:BF:A5:87:0B", 10))
