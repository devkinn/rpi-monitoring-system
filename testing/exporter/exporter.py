from prometheus_client import start_http_server, Gauge
import random
import time
import threading

def generate_metrics():
    gauges = {}
    num_series = 200000
    for i in range(num_series):
        gauges[i] = Gauge(f"custom_metric{i}", 'A custom metric', ['series'])
        gauges[i].labels(series=f"metric_{i}").set(random.uniform(0, 100))
    return gauges

def expose_metrics():
    start_http_server(8000)
    gauges = generate_metrics()
    while True:
        for i in range(len(gauges)):
            gauges[i].labels(series=f"metric_{i}").set(random.uniform(0, 100))
        time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=expose_metrics, daemon=True).start()
    while True:
        time.sleep(1)