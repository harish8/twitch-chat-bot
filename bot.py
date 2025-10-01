from dotenv import load_dotenv
import os
import httpx

# load variables from .env
load_dotenv() 

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

async def fetch_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://id.twitch.tv/oauth2/token",
            params={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials"
            }
        )
        response.raise_for_status()
        data = response.json()        
        return data["access_token"]
