# bot.py
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import chat

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True
# client = commands.Bot(command_prefix=your_prefix, guild_subscriptions=True, intents=intents)
# client = commands.Bot( guild_subscriptions=True) 

client = discord.Client(guild_subscriptions=True, chunk_guilds_at_startup=True ,intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # print(guild.members)
    # for member in guild.members:
    #     print( member.name , end=" ")

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server friend!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return    

    response = chat.reply(message.content)
    await message.channel.send(response)

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        # else:
        #     raise
client.run(TOKEN)