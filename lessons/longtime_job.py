import json
import time

import requests

respons = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
token_json = json.loads(respons.text)
token = token_json['token']
print(respons.text)
print('*'*30)

respons_1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':token})
print(respons_1.text)
print('*'*30)

time_sleep = token_json["seconds"]+1
time.sleep(time_sleep)
respons_2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={'token':token})
print(respons_2.text)
print('*'*30)
