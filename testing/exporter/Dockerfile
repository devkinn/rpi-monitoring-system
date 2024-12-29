FROM python:3.8-slim

WORKDIR /exporter

COPY exporter.py /exporter

RUN pip install prometheus_client

EXPOSE 8000

CMD ["python", "exporter.py"]