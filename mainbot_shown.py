from keep_alive import keep_alive
import discord
import random
from discord.ext import commands

# Define bot command prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

# List of encouraging messages
encouragements = [
    "You're doing great! Keep it up! (Made by @ace_haxxed on discord)",
    "Believe in yourself, you got this! (Made by @ace_haxxed on discord)",
    "Don't give up, success is near! (Made by @ace_haxxed on discord)",
    "You're amazing just the way you are! (Made by @ace_haxxed on discord)",
    "Keep pushing forward, greatness awaits!(Made by @ace_haxxed on discord)"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send("Hello! Hope you're having a great day! 😊 (Made by @ace_haxxed on discord)")

@bot.command()
async def encourage(ctx):
    await ctx.send(random.choice(encouragements))

@bot.command()
async def raid(ctx):
    for _ in range(100):
        await ctx.send("skibidi @everyone and made by @ace_haxxed on discord")

@bot.command()
async def nuke(ctx):
    for _ in range(100):
        await ctx.send("skibidi @everyone and made by @ace_haxxed on discord")

keep_alive()
# Run the bot (Replace 'YOUR_BOT_TOKEN' with your actual bot token)
bot.run('YOUR_BOT_TOKEN')
