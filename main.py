import requests
import json
from datetime import datetime
from os import getenv
from dotenv import load_dotenv

# load webhook url from .env file
load_dotenv()
WEBHOOK = getenv('WEBHOOK')

URL1 = 'https://cobs.si/api/comet_list.api?cur-mag='
URL2 = '&page=1'
MAG = '12' # filter comets by max current magnitude
URL = URL1 + MAG + URL2
CURRENT_DATE = datetime.today().strftime('%Y-%m-%d')

data = requests.get(URL).json()
comets = data['objects'] # returns a list of dicts with comet info

# put each column into a separate list
fullnames = [i['name'] for i in comets]
currMags = [i['current_mag'] for i in comets]
peakMags = [i['peak_mag'] for i in comets]
peakMagDates = [i['peak_mag_date'] for i in comets]

# find length of each colums
w_fullname = max(len('Full name'), max(len(i) for i in fullnames)) + 2
w_currMag = len('Current magnitude') + 2
w_peakMag = len('Peak magnitude') + 2
w_peakMagDate = len('Peak magnitude date') + 2

# build header and separator
header = f'| {'Full name':<{w_fullname}} | {'Current magnitude':<{w_currMag}} | {'Peak magnitude':<{w_peakMag}} | {'Peak magnitude date':<{w_peakMagDate}} |'
separator = '|' + '-'*w_fullname + '|' + '-'*w_currMag + '|' + '-'*w_peakMag + '|' + '-'*w_peakMagDate + '|'

# build rows
rows = []
for a, b, c, d in zip(fullnames, currMags, peakMags, peakMagDates):
    rows.append(f'|{a:<{w_fullname}}|{b:<{w_currMag}}|{c:<{w_peakMag}}|{d:<{w_peakMagDate}}|')

table = '\n'.join(['```', header, separator] + rows + ['```']) # put all elements into one list and join them with newline characters

payload = {'content': table}

response = requests.post(WEBHOOK, json=payload)
print(response.status_code)