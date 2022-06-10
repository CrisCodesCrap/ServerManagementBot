from main import bot, load_dotenv, getenv

load_dotenv()
TOKEN = getenv("TOKEN")

bot.run(TOKEN)