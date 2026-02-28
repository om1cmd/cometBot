import requests
from datetime import datetime, timedelta
from os import getenv
from dotenv import load_dotenv

# load webhook url from .env file
load_dotenv()
WEBHOOK = getenv('WEBHOOK')

URL1 = 'https://cobs.si/api/comet_list.api?cur-mag='
URL2 = '&page=1'
MAG = '15' # filter comets by max current magnitude
URL = URL1 + MAG + URL2

data = requests.get(URL).json()
comets = data['objects'] # returns a list of dicts with comet info
print(len(comets))

# filter comets by peak_mag_date
oneWeekAgo = datetime.today() - timedelta(days=7)

filteredComets = []
for comet in comets:
    peak_mag_date = datetime.strptime(comet['peak_mag_date'], '%Y-%m-%d')
    peak_mag = comet['peak_mag']
    if peak_mag_date >= oneWeekAgo and peak_mag < '10':
        filteredComets.append(comet)

#sort comets by peak_mag_date
sortedComets = sorted(filteredComets, key=lambda comet: datetime.strptime(comet['peak_mag_date'], '%Y-%m-%d'), reverse=False)

def table(sortedComets):
    # put each column into a separate list
    fullnames = [i['fullname'] for i in sortedComets]
    currMags = [i['current_mag'] for i in sortedComets]
    peakMags = [i['peak_mag'] for i in sortedComets]
    peakMagDates = [i['peak_mag_date'] for i in sortedComets]

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
    return table

content = table(sortedComets)
payload = {'content': content}

response = requests.post(WEBHOOK, json=payload)
print(response.status_code)