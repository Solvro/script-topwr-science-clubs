import os

from directus_sdk_py import DirectusClient

from dotenv import load_dotenv

load_dotenv()
client = DirectusClient(
    url=os.getenv("DIRECTUS_URL"), token=os.getenv("DIRECTUS_TOKEN")
)
