from aranet4 import client
import datetime
import sys


def store_scan_result(advertisement):
    global found
    if not advertisement.device:
        return

    found[advertisement.device.address] = advertisement


found = {}
print("Looking for Aranet devices...")
devices = client.find_nearby(store_scan_result)
print(f"Scan finished. Found {len(devices)}")
print()
for _, advertisement in found.items():
    if advertisement.readings:
        print(advertisement.readings.toString(advertisement))
    else:
        print("=======================================")
        print(f"  Name:     {advertisement.device.name}")
        print(f"  Address:  {advertisement.device.address}")
        print(f"  RSSI:     {advertisement.rssi} dBm")
        print()
    print()