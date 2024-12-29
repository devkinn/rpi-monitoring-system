FROM python:3.8-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask prometheus_client

EXPOSE 5000
EXPOSE 8000

CMD ["python", "app.py"]
