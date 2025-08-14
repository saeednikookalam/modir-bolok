# Modir Bolok - Bale Bot

A Bale bot application built with FastAPI and python-bale-bot.

## Features

- FastAPI integration for webhook support
- Message handling with command support (/start, /help, /menu)
- Inline keyboard support with callback handling
- Both long polling and webhook modes
- Docker support

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file from example:
```bash
cp .env .env
```

3. Add your Bale bot token to `.env`:
```
BALE_BOT_TOKEN=your_bot_token_here
```

Get your bot token from @botfather in Bale.

## Running the Bot

### Option 1: Run bot directly (long polling)
```bash
python main.py
```

### Option 2: Run with FastAPI (webhook support)
```bash
uvicorn src.app:app --reload
```

### Option 3: Run with Docker
```bash
docker build -t modir-bolok .
docker run -p 8000:8000 --env-file .env modir-bolok
```

## Bot Commands

- `/start` - Welcome message
- `/help` - Show help
- `/menu` - Display inline keyboard menu

## API Endpoints

- `GET /` - API status
- `GET /health` - Health check
- `POST /webhook` - Webhook endpoint for Bale updates

## Project Structure

```
modir-bolok/
├── src/
│   ├── app.py       # FastAPI application
│   ├── bot.py       # Bot logic and handlers
│   └── config.py    # Configuration management
├── main.py          # Standalone bot runner
├── Dockerfile       # Docker configuration
├── requirements.txt # Python dependencies
└── .env.example     # Environment variables template
```