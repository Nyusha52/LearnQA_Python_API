import requests

respons = requests.post('https://playground.learnqa.ru/api/long_redirect')
first_response = respons.history
for i in range(len(first_response)):
    print(first_response[i])
    print(first_response[i].url)
print(respons.status_code)
print(respons.url)
