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
│   ├── bot.py             # Main bot logic and message handlers (BASIC IMPLEMENTATION ONLY)
│   └── config/
│       └── config.py      # Configuration and environment variables
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration for deployment
├── README.md             # User documentation
└── CLAUDE.md             # This file - developer documentation

MISSING FILES:
├── main.py                # NOT IMPLEMENTED - Standalone bot runner
├── test_webhook.py        # NOT IMPLEMENTED - Webhook testing script
└── .env                   # NOT CREATED - Environment variables file
```

## Core Components

### 1. Bot Class (`src/bot.py`)
- **BaleBot class**: Basic bot initialization with token
- **Current Implementation**:
  - Constructor that validates config and creates Bot instance
  - `process_update()` method that only logs and returns True
  - Singleton pattern via `get_bot()` function
- **NOT IMPLEMENTED**:
  - Message handlers for `/start`, `/help`, `/menu` commands
  - Callback handlers for inline keyboards
  - Actual message processing logic
  - Connection to Bale API for sending messages

### 2. FastAPI Application (`src/app.py`)
- **Current Implementation**:
  - Basic FastAPI app setup
  - `GET /` - API status check (working)
  - `GET /health` - Health check endpoint (working)
  - `POST /webhook` - Receives webhook updates and calls bot.process_update()
- **Issues**:
  - No lifespan management implemented
  - Webhook endpoint just passes data to bot without validation
  - No actual webhook registration with Bale API

### 3. Configuration (`src/config/config.py`)
- **Current Implementation**:
  - Config class with validate() method
  - Loads environment variables using dotenv
  - Gets BALE_BOT_TOKEN from environment
- **Issue**:
  - .env file doesn't exist yet (needs to be created with token)

### 4. Standalone Runner (`main.py`)
- **STATUS**: NOT IMPLEMENTED
- Referenced in documentation but file doesn't exist
- Would run bot in long polling mode

## Bot Features (PLANNED - NOT IMPLEMENTED)

### Message Handling
- **NOT IMPLEMENTED**: Text message processing
- **NOT IMPLEMENTED**: Command recognition and routing
- **NOT IMPLEMENTED**: Echo functionality for non-command messages
- **NOT IMPLEMENTED**: Persian language interface

### Interactive Elements
- **NOT IMPLEMENTED**: Inline keyboards
- **NOT IMPLEMENTED**: Callback query handling
- **NOT IMPLEMENTED**: Dynamic menu system

### Update Processing
- **PARTIAL**: Receives updates but doesn't process them
- **NOT IMPLEMENTED**: Message handling
- **NOT IMPLEMENTED**: Callback query handling

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
- **NOT IMPLEMENTED**: `test_webhook.py` file doesn't exist
- No test files or test infrastructure currently in place

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

## Current Project Status

### What's Working:
- Basic FastAPI application structure
- Webhook endpoint receives POST requests
- Configuration loads from environment variables
- Bot class initialization with Bale token

### What's NOT Working:
- No actual bot functionality implemented
- No message handlers or command processing
- No connection to Bale API for sending messages
- Missing main.py for long polling mode
- Missing test files
- Missing .env file

### Immediate TODOs:
1. Create .env file with BALE_BOT_TOKEN
2. Implement actual message handling in bot.py
3. Add command handlers (/start, /help, /menu)
4. Implement sending messages via Bale API
5. Create main.py for long polling mode
6. Add test_webhook.py for testing
7. Implement inline keyboards and callbacks

## Notes for Developers
- The bot instance is singleton (single instance throughout app lifecycle)
- Currently just a skeleton - needs full implementation
- All text responses should be in Persian (Farsi)
- The bot should handle both private and group chats
- Callback data should be kept short (max 64 bytes in Bale)