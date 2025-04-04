import aranet4
import sys


sys.coinit_flags = 0  # 0 means MTA
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
    try:
        from bleak.backends.winrt.util import allow_sta
        # tell Bleak we are using a graphical user interface that has been properly
        # configured to work with asyncio
        allow_sta()
        reading = aranet4.client.get_current_readings(device_mac)
        print("Finished getting record.")
        return reading
    except ImportError:
        # other OSes and older versions of Bleak will raise ImportError which we
        # can safely ignore
        pass

