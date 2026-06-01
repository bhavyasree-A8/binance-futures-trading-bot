from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")

print("API Key Found:", api_key is not None)
print("Secret Key Found:", secret_key is not None)

print("API Key Length:", len(api_key))
print("Secret Key Length:", len(secret_key))