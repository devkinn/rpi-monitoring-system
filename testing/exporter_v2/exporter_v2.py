from prometheus_client import start_http_server, Gauge
import random
import time

def generate_metrics(count):
    metrics = []
    for i in range(count):
        metric = Gauge(f"metric_{i}", "Custom metric")
        metric.set(random.uniform(0, 100))
        metrics.append(metric)
    return metrics

def expose_metrics():
    start_http_server(8000)
    metric_count = 10000

    metrics = generate_metrics(metric_count)
    print(f"Generated {len(metrics)} metrics.")

    while True:
        time.sleep(60)
        for metric in metrics:
            metric.set(random.uniform(0, 100))
        print(f"Generated new values for {len(metrics)} metrics.")

if __name__ == "__main__":
    expose_metrics()