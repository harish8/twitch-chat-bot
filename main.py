from fastapi import FastAPI
from bot import fetch_token

app = FastAPI()

# Get an Oauth token from Twitch
@app.get("/get-token")
async def get_token():
    return await fetch_token()


