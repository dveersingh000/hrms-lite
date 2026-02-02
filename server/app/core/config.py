import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI") # type: ignore
    APP_NAME: str = "HRMS Lite API"

settings = Settings()
