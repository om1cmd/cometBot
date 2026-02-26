import requests
import time
import json
from rich import print
from types import SimpleNamespace
from datetime import datetime
import discord
from discord.ext import commands

prefix = 'cm'
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents)

URL1 = 'https://cobs.si/api/comet_list.api?cur-mag='
URL2 = '&page=1'
MAG = '12' # filter comets by max current magnitude
DATE = datetime.today().strftime('%Y-%m-%d')

def json_to_obj(json_str: str) -> object:
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))

def ct():
    t = time.localtime()
    return time.strftime('%H:%M:%S', t)

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name='Looking for comets')
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'\n[{ct()}] Bot initialized')

@client.command()
async def comets(ctx, mag=None):
    if mag is None:
        await ctx.send(f'Correct usage is `{prefix}comets *min_magnitude*`')
        return

    URL = URL1 + mag + URL2
    data = json_to_obj(requests.get(URL).text)

    answer = '**Comet name**, **Current magnitude**, **Peak magnitude**, **Peak magnitude date**\n'
    for obj in data():
        line = obj.fullname + ', ' + obj.current_mag + ', ' + obj.peak_magnitude + ', ' + obj.peak_magnitude_date + '\n'
        answer += line

client.run('MTQ3NjY5MTg3MjcyNTM0MDM3MQ.GP4HWA.t3vEoGqv5IIAt0PNX66U53DZFma9jZmuzO0gc4')