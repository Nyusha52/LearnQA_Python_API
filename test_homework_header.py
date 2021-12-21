from datetime import datetime, timedelta

import requests


class TestHeader:
    def test_header(self):
        respons = requests.get('https://playground.learnqa.ru/api/homework_header')
        now = datetime.now()+timedelta(hours=-3)
        n = now.strftime("%a, %d %b %Y %X")
        header_respons = {'Date': f'{n} GMT', 'Content-Type': 'application/json', 'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache', 'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0', 'Expires': f'{n} GMT'}
        assert header_respons == dict(respons.headers)
