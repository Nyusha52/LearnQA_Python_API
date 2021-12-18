import requests
class TestCookie:
    def test_cookie(self):
        respons = requests.get('https://playground.learnqa.ru/api/homework_cookie')
        cookies_respons = dict(respons.cookies)
        print(cookies_respons)
        assert cookies_respons == dict(respons.cookies)
