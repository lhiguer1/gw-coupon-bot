import os
import sys
from discord.ext import commands
from dotenv import load_dotenv

initial_extensions = [
    'gw_coupon',
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

sys.path.insert(1, os.getcwd() + "/cogs/")

for extension in initial_extensions:
    bot.load_extension(extension)

bot.run(TOKEN)