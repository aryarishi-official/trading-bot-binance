import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key=os.getenv("API_KEY")
    api_secret=os.getenv("API_SECRET")

    if(not api_key or not api_secret):
        raise ValueError("API_KEY and API_SECRET must be set in the .env file")
    client=Client(api_key,api_secret)
    client.API_URL = "https://testnet.binance.vision/api"
    return client
