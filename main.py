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
fullnames = [i['fullname'] for i in comets]
currMags = [i['current_mag'] for i in comets]
peakMags = [i['peak_mag'] for i in comets]
peakMagDates = [i['peak_mag_date'] for i in comets]

# find length of each colums
padd = 2
w_fullname = max(len('Full comet name'), max(len(i) for i in fullnames)) + padd
w_currMag = len('Current mag') + padd
w_peakMag = len('Peak mag') + padd
w_peakMagDate = len('Peak mag date') + padd

# build header and separator
header = f'|{'Full comet name':^{w_fullname}}|{'Current mag':^{w_currMag}}|{'Peak mag':^{w_peakMag}}|{'Peak mag date':^{w_peakMagDate}}|'
separator = '|' + '-'*w_fullname + '|' + '-'*w_currMag + '|' + '-'*w_peakMag + '|' + '-'*w_peakMagDate + '|'

# build rows
rows = []
for a, b, c, d in zip(fullnames, currMags, peakMags, peakMagDates):
    rows.append(f'|{a:^{w_fullname}}|{b:^{w_currMag}}|{c:^{w_peakMag}}|{d:^{w_peakMagDate}}|')

table = '\n'.join(['```', header, separator] + rows + ['```']) # put all elements into one list and join them with newline characters

payload = {'content': table}

response = requests.post(WEBHOOK, json=payload)
print(response.status_code)