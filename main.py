import discord
from discord import app_commands
from discord.interactions import Interaction
from dotenv import load_dotenv
from discord.utils import get
from os import getenv
load_dotenv()

guildId = getenv("GUILD_ID")
token = getenv("TOKEN")
joinRoleId = getenv("JOIN_ROLE_ID")

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
    
    async def on_ready(self):
        if not self.synced:
            await commands.sync(guild=discord.Object(id=guildId))
            print(f"Bot instance ready and synced to server {guildId}")

bot = Bot()
commands = app_commands.CommandTree(bot)

@bot.event
async def on_member_join(ctx):
  role = get(ctx.guild.roles, id=joinRoleId)
  await ctx.add_roles(role)
  

@commands.command(name="clear", description="Clears the chat.", guild=discord.Object(id=guildId))
async def self(ctx:Interaction, amount:str):
    if amount == "all":
        await ctx.response.send_message("Clearing chat...")
        await ctx.channel.purge(limit=None)
    elif amount.isnumeric():
        await ctx.response.send_message("Clearing the last {} messages...".format(amount))
        await ctx.channel.purge(limit=int(amount))
    else:
        msg = await ctx.response.send_message("Please enter a number or 'all' to execute the command.")
        await deleteMsg(msg)
async def deleteMsg(msg):
    await msg.delete(delay=5)