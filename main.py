import os
from chemistryWords import chemistry_words
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print('Chemistry Checker is now running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    string = message.content
    string = string.lower().split(" ")

    for word in string:
        if word in chemistry_words:
            await message.channel.send('You just used the chemistry term: ' + '*' + word + '*')
            await message.channel.send('Go back to the lab!')

client.run(TOKEN)