import discord
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client) #This tree contains all the commands written, not super necessary right now but scalable.

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=246483365832687619))
    print(f'We have logged in as {client.user}')

#Makes sure the bot doesn't respond to istelf
@client.event
async def on_message(message):
    if message.author == client.user:
        return

@tree.command(name = "ammo", description = "search for an ammo type", guild=discord.Object(id=246483365832687619)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def ammo_command(ctx):
    return

TOKEN = os.getenv('TOKEN')
client.run(TOKEN)