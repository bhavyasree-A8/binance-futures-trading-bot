from dotenv import load_dotenv
from binance.client import Client
import os


class BinanceClient:

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        secret_key = os.getenv("SECRET_KEY")

        self.client = Client(
            api_key=api_key,
            api_secret=secret_key,
            testnet=True
        )

    def get_server_time(self):
        return self.client.get_server_time()