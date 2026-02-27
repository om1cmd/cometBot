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

data = requests.get(URL).text

response = requests.post(WEBHOOK, json=data)
print(response.status_code)