import aranet4
import datetime
import csv

file_name = "aranet_history.csv"
device_mac = "60:C0:BF:A5:87:0B"
entry_filter = {
    "last": 5
}


def getAllRecords():
    print("Starting download")
    foundRecords = aranet4.client.get_all_records(device_mac, entry_filter, remove_empty=True)
    print("Finished download")
    return foundRecords



print("")

with open(file_name, 'w') as file:
    records = getAllRecords()
    print("Writing to CSV")
    writer = csv.writer(file)

    header = [
        "date",
        "co2",
        "temperature",
        "humidity",
        "pressure"
    ]

    # Write CSV header
    writer.writerow(header)

    # Write CSV rows
    for line in records.value:
        row = [
            line.date.isoformat(),
            line.co2,
            line.temperature,
            line.humidity,
            line.pressure
        ]

        writer.writerow(row)
    print("Finished writing to: " + file_name)