from prometheus_client import start_http_server, Counter
import time

# Create a metric
requests_total = Counter('requests_total', 'Total requests')

# Increment the metric
requests_total.inc()

# Start the metrics server
start_http_server(8000)

while True:
    print("Server is running at localhost:8000. Press Ctrl+C to stop.")
    time.sleep(10)