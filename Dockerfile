FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app/src

RUN apt-get update && apt-get install -y curl

RUN pip install --no-cache-dir uv

COPY requirements.txt .

RUN uv pip install --system --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]