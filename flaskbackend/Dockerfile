FROM python:3.9

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir opentelemetry-exporter-jaeger

COPY . .

CMD ["python", "app.py"]

EXPOSE 5000
