from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

print("Connecting to Binance...")

client = Client(
    api_key=api_key,
    api_secret=secret_key,
    testnet=True
)

server_time = client.get_server_time()

print("Connected Successfully!")
print("Server Time:", server_time)