FROM python:3.8-slim

WORKDIR /exporter_v2

COPY exporter_v2.py /exporter_v2

RUN pip install prometheus_client

EXPOSE 8000

CMD ["python", "-u", "exporter_v2.py"]