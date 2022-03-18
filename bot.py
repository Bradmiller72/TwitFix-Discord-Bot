import discord
import requests
from datetime import date, datetime
from datetime import timedelta
from ratelimit import limits, sleep_and_retry
import re
import json
import os
os.environ['TZ'] = "America/Chicago"
import random

EIGHT_SECONDS = 8

client = discord.Client()
token = os.environ.get("DISCORD_BOT_TOKEN")
twitter_string = "https://twitter.com"
fxtwitter_string = "https://fxtwitter.com"
pattern = re.compile(r"(https:\/\/twitter.com[^\s\,]+)")

X_WEIGHT = 8

def is_twitter_comment(comment):
    m = pattern.search(comment)
    if(m):
        return m.group(0).replace(twitter_string, fxtwitter_string)
    else:
        return None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    reply_message =  is_twitter_comment(message.content)
    if reply_message:
        await message.reply(content=reply_message)

    print('Message from {0.author}: {0.content}'.format(message))

client.run(token)