from fastapi import FastAPI, HTTPException
from bot import get_bot
from models import UpdateParser
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
        # Parse the raw update data to Update object
        update = UpdateParser.parse_update(update_data)

        if not update:
            logger.error(f"Failed to parse update: {update_data}")
            raise HTTPException(status_code=400, detail="Invalid update format")

        logger.info(f"Processing update {update.update_id} of type: {UpdateParser.get_update_type(update_data)}")

        # Process the update
        bot = get_bot()
        success = await bot.process_update(update)

        if success:
            return {"status": "success", "update_id": update.update_id}
        else:
            raise HTTPException(status_code=400, detail="Failed to process update")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
