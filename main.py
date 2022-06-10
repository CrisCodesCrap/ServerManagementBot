import discord
from discord import app_commands
from discord.interactions import Interaction
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
    
    async def on_ready(self):
        if not self.synced:
            await commands.sync(guild=discord.Object(id=getenv("GUILD_ID")))
            print("Bot instance ready and synced.")

bot = Bot()
commands = app_commands.CommandTree(bot)