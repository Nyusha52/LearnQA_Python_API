import requests


class TestHeader:
    def test_header(self):
        respons = requests.get('https://playground.learnqa.ru/api/homework_header')
        header_respons = dict(respons.headers)
        print(header_respons)
        assert header_respons == dict(respons.headers)
