import time
from prometheus_client import start_http_server, Gauge, CollectorRegistry
import Aranet4DataReader


def set_CO2_data():
    val = Aranet4DataReader.getCurrentReading().co2
    print("CO2 reading is " + str(val))
    g.set(val)   # Set to a given value


# Main process
g = Gauge('CO2_PPM', 'CO2 PPM from Aranet4 Sensor')
set_CO2_data()
print("Starting metrics endpoint")
start_http_server(8000)
while True:
    print("Waiting 30 seconds to read")
    time.sleep(30)
    set_CO2_data()
