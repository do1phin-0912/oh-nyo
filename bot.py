import discord
from discord import app_commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    
    channel = client.get_channel(1015375154194436126)
    await channel.send(f'{member.mention} join')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1015375154194436126)
    await channel.send(f'{member.mention} leave')
   
client.run(jdata['token'])

