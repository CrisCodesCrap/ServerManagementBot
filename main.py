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
  

@commands.command(name="hi", description="Says hi the the person you specify", guild=discord.Object(id=guildId))
async def self(interaction:Interaction):
    await interaction.response.send_message('Hi, ' + interaction.user.mention)
    