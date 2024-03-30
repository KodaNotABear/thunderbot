import discord
import os

from discord.ext import commands
from openai import OpenAI
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

apiClient = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

tree = app_commands.CommandTree(
    client)  # This tree contains all the commands written, not super necessary right now but scalable.

guild_ID = 246483365832687619


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_ID))
    print(f'We have logged in as {client.user}')


# Makes sure the bot doesn't respond to istelf
@client.event
async def on_message(message):
    if message.author == client.user:
        return


@tree.command(name="ammo", description="search for an ammo type", guild=discord.Object(
    # Add the guild ids in which the slash command will appear.
    # If it should be in all, remove the argument, but note that
    # it will take some time (up to an hour) to register the command if it's for all guilds.
    id=guild_ID))
async def ammo_command(ctx):
    return


@tree.command(name="thunderbot", description="Talk to ThunderBot", guild=discord.Object(id=guild_ID))
async def chat_with_gpt(ctx, prompt: str):
    response = apiClient.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )


    embed = discord.Embed(title=f'User: {prompt}',
                          description=response.choices[0].message.content.strip(), color=0xff0000)
    embed.set_author(name="ThunderBot",
                     icon_url="https://cdn.discordapp.com/attachments/324410094794047488/1223509867608805467/Untitled-3.png?ex=661a1d5c&is=6607a85c&hm=e2bc087ca4f83b1f7df9a2888bde019c04b1b77f992dd35c2db452b304bd4690&")

    await ctx.response.send_message(embed=embed)




TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
