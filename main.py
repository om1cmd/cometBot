import requests
import time
import json
from rich import print
from types import SimpleNamespace
from datetime import datetime
import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='cm', intents=intents)

def ct():
    t = time.localtime()
    return time.strftime('%H:%M:%S', t)

@client.event
async def on_ready():
    print(f'\n[{ct()}] Bot initialized')
    activity = discord.Activity(type=discord.ActivityType.playing, name='Looking for comets')
    await client.change_presence(status=discord.Status.online, activity=activity)

URL1 = 'https://cobs.si/api/comet_list.api?cur-mag='
URL2 = '&page=1'
MAG = '12' # filter comets by max current magnitude
DATE = datetime.today().strftime('%Y-%m-%d')
URL = URL1 + MAG + URL2

def json_to_obj(json_str: str) -> object:
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))

data = json_to_obj(requests.get(URL).text)
for obj in data.objects:
    print(obj.fullname, obj.peak_mag, obj.peak_mag_date)

client.run('MTQ3NjY5MTg3MjcyNTM0MDM3MQ.GP4HWA.t3vEoGqv5IIAt0PNX66U53DZFma9jZmuzO0gc4')