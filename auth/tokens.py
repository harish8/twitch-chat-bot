from dotenv import load_dotenv
import httpx
import logging
import os

# load variables from .env
load_dotenv() 

LOGGER: logging.Logger = logging.getLogger(__name__)

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

async def get_app_token(client_id: str, client_secret: str) -> str:
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, data=data, timeout=10.0)
        resp.raise_for_status()
        return resp.json()["access_token"]
    
# python -c "import asyncio, tokens; asyncio.run(tokens.refresh_access_token('<refresh_token>'))" 
async def refresh_access_token(refresh_token: str) -> str:
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id":client_id,
        "client_secret":client_secret,
        "grant_type":"refresh_token",
        "refresh_token": refresh_token
    }

    print (f" data:{data}")
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, data=data,timeout=10.0)
        resp.raise_for_status()
        return resp.json()["access_token"]
