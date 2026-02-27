import requests
import time
import json
from rich import print
from datetime import datetime
from types import SimpleNamespace
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

# def json_to_obj(json_str: str) -> object:
#     return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))


# data = json_to_obj(requests.get(URL).text)

# answer = '**Comet name**, **Current magnitude**, **Peak magnitude**, **Peak magnitude date**\n\n'
# for obj in data.objects:
#     line = obj.fullname + ', ' + obj.current_mag + ', ' + obj.peak_mag + ', ' + obj.peak_mag_date + '\n'
#     answer += line

data = {
    'content': 'test',
}

response = requests.post(WEBHOOK, json=data)
print(response.status_code)