import discord
from discord.ext import commands
import random

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

# ask a question and get a random response
@client.command(aliases = ["8ball", "eightball", "eight ball", "8 ball"])
async def magic_eightball(ctx, *, question):
    with open("02/responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
    await ctx.send(response)

# token
client.run("MTA3ODQzOTE4OTU0MjA3NjQ5Ng.GeKZrv.7MKRwGLQ8zFF2FdQFFwpA7lzAjDV_ZUD4ObBv8")