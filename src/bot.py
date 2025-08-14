import logging
from bale import Bot
from config.config import config
from models import Update

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaleBot:
    def __init__(self):
        config.validate()
        self.bot = Bot(token=config.BALE_BOT_TOKEN)

    @staticmethod
    async def process_update(update: Update) -> bool:
        """
        Process incoming update
        
        Args:
            update: Update object from webhook
            
        Returns:
            True if processed successfully, False otherwise
        """
        try:
            # Handle message
            if update.message:
                return True

            # Handle edited message
            elif update.edited_message:
                return True

            # Handle callback query
            elif update.callback_query:
                return True

            # Handle channel post
            elif update.channel_post:
                return True

            # Handle edited channel post
            elif update.edited_channel_post:
                return True

            else:
                logger.warning(f"Unknown update type: {update.update_id}")
                return False

        except Exception as e:
            logger.error(f"Error processing update {update.update_id}: {e}")
            return False


bot_instance = None


def get_bot():
    global bot_instance
    if bot_instance is None:
        bot_instance = BaleBot()
    return bot_instance
