# Modir Bolok - Bale Bot Project

## Project Overview
This is a Bale bot application built with FastAPI and python-bale-bot library. The bot supports both webhook and long polling modes for receiving updates from Bale messaging platform.

## Technology Stack
- **Python 3.12**
- **FastAPI** - Web framework for webhook endpoint
- **python-bale-bot** - Official Bale bot library
- **aiohttp** - Async HTTP client/server
- **python-dotenv** - Environment variable management

## Project Structure

```
modir-bolok/
├── src/                    # Source code directory
│   ├── app.py             # FastAPI application with webhook endpoint
│   ├── bot.py             # Main bot logic and message handlers
│   └── config.py          # Configuration and environment variables
├── main.py                # Standalone bot runner (long polling mode)
├── test_webhook.py        # Webhook testing script
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration for deployment
├── README.md             # User documentation
├── CLAUDE.md             # This file - developer documentation
└── .env.example          # Environment variables template
```

## Core Components

### 1. Bot Class (`src/bot.py`)
- **BaleBot class**: Main bot implementation
- **Message handlers**: 
  - `/start` - Welcome message
  - `/help` - Help information
  - `/menu` - Interactive inline keyboard menu
- **Callback handlers**: Process button clicks from inline keyboards
- **Webhook support**: `process_webhook_update()` method for handling webhook updates
- **Dual mode operation**: Supports both webhook and long polling modes

### 2. FastAPI Application (`src/app.py`)
- **Lifespan management**: Initializes bot on startup, cleanup on shutdown
- **Endpoints**:
  - `GET /` - API status check
  - `GET /health` - Health check endpoint
  - `POST /webhook` - Receives and processes Bale webhook updates
- **Webhook mode**: Bot runs in webhook mode when started via FastAPI

### 3. Configuration (`src/config.py`)
- Loads environment variables from `.env` file
- Validates required configuration (BALE_BOT_TOKEN)
- Centralized configuration management

### 4. Standalone Runner (`main.py`)
- Runs bot in long polling mode
- Direct execution without web server
- Suitable for development and simple deployments

## Bot Features

### Message Handling
- Text message processing
- Command recognition and routing
- Echo functionality for non-command messages
- Persian language interface

### Interactive Elements
- Inline keyboards with multiple buttons
- Callback query handling for button interactions
- Dynamic menu system

### Update Processing
- Supports message updates
- Handles callback queries
- Logs edited messages

## Running Modes

### 1. Long Polling Mode
```bash
python main.py
```
- Bot actively fetches updates from Bale servers
- No external URL required
- Good for development and testing

### 2. Webhook Mode
```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
```
- Bale sends updates to your server
- Requires public HTTPS URL
- Better for production deployments

## Environment Variables
Required in `.env` file:
- `BALE_BOT_TOKEN` - Bot token from @botfather in Bale

## Testing
- `test_webhook.py` - Tests webhook endpoint with sample updates
- Includes health check and webhook update simulation

## Development Commands

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run tests
```bash
python test_webhook.py
```

### Development server
```bash
uvicorn src.app:app --reload
```

### Production deployment
```bash
uvicorn src.app:app --host 0.0.0.0 --port 8000 --workers 4
```

## Docker Deployment
```bash
docker build -t modir-bolok .
docker run -p 8000:8000 --env-file .env modir-bolok
```

## API Integration
The bot uses Bale's API which is similar to Telegram Bot API:
- Base URL: `https://tapi.bale.ai/bot<token>/`
- Supports both GET and POST methods
- JSON response format
- Webhook and long polling update methods

## Error Handling
- Comprehensive try-catch blocks in webhook processing
- Logging for debugging and monitoring
- Graceful fallback for unknown commands/callbacks

## Security Considerations
- Token stored in environment variables
- Input validation for webhook updates
- Error messages don't expose sensitive information

## Future Enhancements
- Database integration for user data persistence
- Advanced conversation flows with state management
- Payment processing capabilities
- File upload/download support
- Multi-language support
- Admin panel for bot management
- Analytics and usage tracking

## Notes for Developers
- The bot instance is singleton (single instance throughout app lifecycle)
- Webhook mode is automatically enabled when running via FastAPI
- All text responses are in Persian (Farsi)
- The bot handles both private and group chats
- Callback data should be kept short (max 64 bytes in Bale)