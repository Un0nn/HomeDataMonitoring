import asyncio
import time

import aranet4.client
from aranet4.client import Aranet4Advertisement
from bleak import BleakScanner


async def get_current_reading(aranet4_mac: str = None):
    """
    Will scan for Aranet4 advertisements until target device is found or any aranet device is found.
    :param aranet4_mac: Optional MAC address of target aranet4 device.
    :return: Current reading data
    """
    stop_event = None
    current_reading: list[aranet4.client.CurrentReading] = [None]

    def callback(device, ad_data):
        if device.address == aranet4_mac:
            adv = Aranet4Advertisement(device, ad_data)
            print("Found specified Aranet4.")
            if adv:
                current_reading[0] = adv.readings
            stop_event.set()

    while True:
        stop_event = asyncio.Event()
        async with BleakScanner(callback):
            print("\nScanner started")

            await stop_event.wait()  # wait for correct device in callback
            print("Scanner stopped.\n")

        return current_reading[0]


async def scan_aranet4_device(aranet4_mac: str, scrape_interval: int, callback):
    """
    Scans aranet device, waiting scrape_interval seconds between scans
    scrape_interval is only the wait time, so expect the time between data to be a couple seconds longer than scrape_interval
    """
    stop_event = None

    def callback(device, ad_data):
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

            await stop_event.wait()  # wait for correct device in callback
            print("Scanner stopped.")

        time.sleep(scrape_interval)
