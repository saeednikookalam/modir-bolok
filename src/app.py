from fastapi import FastAPI, HTTPException
from bot import get_bot
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bale Bot API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "bot": "running"}


@app.post("/webhook")
async def webhook(update_data: dict):
    try:
        # Process the update
        bot = get_bot()
        success = await bot.process_update(update_data)

        if success:
            return {"status": "success"}
        else:
            raise HTTPException(status_code=400, detail="Failed to process update")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
