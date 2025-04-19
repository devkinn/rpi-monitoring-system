# rpi-monitoring system

Prometheus-Alertmanager-Grafana-Cadvisor monitoring stack ready to deploy on a Raspberry Pi.

The whole monitoring system is set up based of off USE and RED monitoring methodologies which are applied for Grafana dashboards and Alertmanager alert generation.

The whole project is setup using containers and Docker Compose to enable easy replication.

Directory `testing` contains custom Prometheus exporters written in Python for benchmarking the monitoring system. They can be easily deployed using Ansible playbooks stored in `playbooks` directory.
