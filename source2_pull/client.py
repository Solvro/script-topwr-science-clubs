import os

from directus_sdk_py import DirectusClient

from dotenv import load_dotenv

load_dotenv()
client = DirectusClient(url=os.getenv("SOURCE2_DIRECTUS_URL"))
