import aranet4
import datetime
import time


device_mac = "60:C0:BF:A5:87:0B"
entry_filter = {
    "last": 3
}


def getAllRecords():
    print("Starting download")
    foundRecords = aranet4.client.get_all_records(device_mac, entry_filter, remove_empty=True)
    print("Finished download")
    return foundRecords


def getCurrentReading():
    print("Getting current record.")
    reading = aranet4.client.get_current_readings(device_mac)
    print("Finished getting record.")
    return reading


current = getCurrentReading()
print(current.co2)
