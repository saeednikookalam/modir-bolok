FROM python:3.12-slim

WORKDIR /app

# ENVs
ENV PYTHONPATH=/app/src

RUN apt install curl

# INstall uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY requirements.txt .

RUN uv pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]