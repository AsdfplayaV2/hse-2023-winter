# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

CMD ["python", "app.py"]
