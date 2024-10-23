import os
from dotenv import load_dotenv

load_dotenv()

REPLICATE_API_URL = os.getenv("REPLICATE_API_URL", "https://api.replicate.com/v1/predictions")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN", "<Your-Replicate-API-Token>")

