import random
import time
from prometheus_client import start_http_server, Gauge


def set_CO2_data():
    val = random.randint(400, 2000)
    print("CO2 reading is " + str(val))
    g.set(val)   # Set to a given value


g = Gauge('CO2_PPM', 'Description of gauge')
start_http_server(8000)
while True:
    set_CO2_data()
    time.sleep(10)
