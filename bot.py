from dotenv import load_dotenv
from twitchio.ext import commands
import logging
import random
# import httpx
import os

# load variables from .env
load_dotenv() 

LOGGER: logging.Logger = logging.getLogger(__name__)


client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
bot_id = os.getenv("BOT_ID")

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=f"oauth:{os.getenv('TWITCH_OAUTH_TOKEN')}",
            prefix="!",
            initial_channels=["horionx88"]
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        
    async def event_message(self, message):
        if message.echo:
            return
        
        # print(f"DEBUG: Got message: {message.content} from {message.author.name}")
        print(f"{message.author.name}: {message.content}")  # prints chat to console
        
        # await message.channel.send("Bot received your message!")  # <-- sends a message to the channel
        await self.handle_commands(message)

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command(name="command_name")
    async def command_name(self, ctx):
        names_taken = set()
        
        with open('file_name.txt', 'r') as file:
            names = [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]

        random_name = random.choice(names)
                
        # TODO change the logic to the names_taken shouldn't repeat again in the stream. 
        names_taken.add(random_name)
        await ctx.send(f" Choosen random name : {random_name}")
        
if __name__ == '__main__':
    bot = Bot()
    bot.run()