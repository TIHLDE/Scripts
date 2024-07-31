import os

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")
TIHLDE_API_TOKEN = os.getenv("TIHLDE_API_TOKEN")

TIHLDE_API_URL = "https://api-dev.tihlde.org/" if ENVIRONMENT == "DEV" else "https://api.tihlde.org/"
