from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Counter, Histogram
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter("app_requests_total", "Total requests processed", ["method"])
ERROR_COUNT = Counter("app_errors_total", "Total errors encountered", ["method"])
REQUEST_DURATION = Histogram("app_request_duration_seconds", "Duration of requests in seconds", ["method"])

@app.route("/", methods=["GET"])
def listen():
    start_time = time.time()
    method = "GET"
    REQUEST_COUNT.labels(method=method).inc()
    
    if random.random() < 0.5:
        ERROR_COUNT.labels(method=method).inc()
        return jsonify({"message": "Request error"}), 500

    time.sleep(random.uniform(0.4, 1.0))
    duration = time.time() - start_time
    REQUEST_DURATION.labels(method=method).observe(duration)
    
    return jsonify({"message": "Request success"}), 200

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)