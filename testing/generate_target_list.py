import json

ip_range = ["192.168.10.21", "192.168.10.22", "192.168.10.23", "192.168.10.24"]
port_range = range(9500, 9550)

targets = []
for ip in ip_range:
    for port in port_range:
        targets.append(f"{ip}:{port}")

output = [{"targets": targets}]

filename = "exporter_v2.json"
with open(filename, "w") as f:
    json.dump(output, f, indent=4)

print(f"JSON target list saved to {filename}.")
