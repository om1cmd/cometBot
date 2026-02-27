import requests
import time
import json
from rich import print
from datetime import datetime

URL1 = 'https://cobs.si/api/comet_list.api?cur-mag='
URL2 = '&page=1'
MAG = '12' # filter comets by max current magnitude
DATE = datetime.today().strftime('%Y-%m-%d')

def json_to_obj(json_str: str) -> object:
    return json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))

URL = URL1 + mag + URL2
data = json_to_obj(requests.get(URL).text)

answer = '**Comet name**, **Current magnitude**, **Peak magnitude**, **Peak magnitude date**\n\n'
for obj in data.objects:
    line = obj.fullname + ', ' + obj.current_mag + ', ' + obj.peak_mag + ', ' + obj.peak_mag_date + '\n'
    answer += line
    