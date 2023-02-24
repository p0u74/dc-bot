import discord
from discord.ext import commands
import os
import asyncio

# command type
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run alert
@client.event
async def on_ready():
    print("Bot is run.")

async def load():
    for filename in os.listdir("04/cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            # optional
            print(f"{filename[:-3]} is loaded!")

async def main():
    async with client:
        await load()
        await client.start("TOKEN")

asyncio.run(main())

