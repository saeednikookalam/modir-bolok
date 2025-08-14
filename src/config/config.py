import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BALE_BOT_TOKEN = os.getenv("BALE_BOT_TOKEN")

    debug: bool = True

    @classmethod
    def validate(cls):
        if not cls.BALE_BOT_TOKEN:
            raise ValueError("BALE_BOT_TOKEN is required in environment variables")
        return True


config = Config()
