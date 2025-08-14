import logging
from typing import Dict, Any
from bale import Bot
from config.config import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaleBot:
    def __init__(self):
        config.validate()
        self.bot = Bot(token=config.BALE_BOT_TOKEN)

    @staticmethod
    async def process_update(update: Dict[str, Any]) -> bool:
        """
        Process incoming update

        Args:
            update: Update object from webhook

        Returns:
            True if processed successfully, False otherwise
        """
        try:
            logger.info("Processing update: %s", update)
            return True
        except Exception as e:
            logger.error(f"Error processing update {update}: {e}")
            return False


bot_instance = None


def get_bot():
    global bot_instance
    if bot_instance is None:
        bot_instance = BaleBot()
    return bot_instance
