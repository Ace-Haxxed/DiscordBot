from keep_alive import keep_alive
import discord
import random
from discord.ext import commands

# Define bot command prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

# List of encouraging messages
encouragements = [
    "You're doing great! Keep it up!",
    "Believe in yourself, you got this!",
    "Don't give up, success is near!",
    "You're amazing just the way you are!",
    "Keep pushing forward, greatness awaits!"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send("Hello! Hope you're having a great day! 😊")

@bot.command()
async def encourage(ctx):
    await ctx.send(random.choice(encouragements))

@bot.command()
async def raid(ctx):
    for _ in range(100):
        await ctx.send("skibidi @everyone")

@bot.command()
async def nuke(ctx):
    for _ in range(100):
        await ctx.send("skibidi @everyone")

keep_alive()
# Run the bot (Replace 'YOUR_BOT_TOKEN' with your actual bot token)
bot.run('YOUR_BOT_TOKEN')
