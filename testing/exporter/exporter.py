from prometheus_client import start_http_server, Gauge, CollectorRegistry, generate_latest
import random
import time

registry = CollectorRegistry()

def generate_metrics(prefix, count, registry):
    metrics = []
    for i in range(count):
        metric = Gauge(f"{prefix}_metric_{i}", "Custom metric for scalability testing", registry=registry)
        metric.set(random.uniform(0, 100))
        metrics.append(metric)
    return metrics

def unregister_metrics(metrics, registry):
    for metric in metrics:
        registry.unregister(metric)

def expose_metrics():
    start_http_server(8000, registry=registry)
    batch_metric_count = 50000
    batch_count = 50

    for i in range(batch_count):
        prefix = f"batch_{i}"
        metrics = generate_metrics(prefix, batch_metric_count, registry)
        print(f"Generated {len(metrics)} metrics for batch {i}.")
        time.sleep(30)
        unregister_metrics(metrics, registry)
        print(f"Unregistered {len(metrics)} metrics for batch {i}.")

    print("Finished generating metrics.")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    expose_metrics()