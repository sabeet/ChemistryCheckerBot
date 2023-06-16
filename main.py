import os

from censor_phrase import censor_phrase
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

    string = message.content.lower()

    for phrase in chemistry_words:
        if phrase.lower() in string:
            censored_text = censor_phrase(phrase, string)
            await message.channel.send(f"{censored_text}")
            await message.channel.send('You just used a STEM term. STEMChecker thanks you for learning')
            break

client.run(TOKEN)