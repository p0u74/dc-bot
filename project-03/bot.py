import discord
from discord.ext import commands, tasks
from itertools import cycle

# command type
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# set bot status
bot_status = cycle(["Status 1", "Status 2", "Status 3", "Status 4"])

# set status loop
@tasks.loop(seconds = 5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

# Run alert
@client.event
async def on_ready():
    print("Bot is run.")
    change_status.start()



# token
client.run("MTA3ODQzOTE4OTU0MjA3NjQ5Ng.GeKZrv.7MKRwGLQ8zFF2FdQFFwpA7lzAjDV_ZUD4ObBv8")