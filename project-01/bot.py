import discord
from discord.ext import commands

# command type
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run alert
@client.event
async def on_ready():
    print("Bot is run.")

# show bot ping
@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.")

# say hi and bot response
@client.command(aliases = ["hello", "hola"])
async def hi(ctx):
    await ctx.send("Hiiiii")

# token
client.run("TOKEN")
