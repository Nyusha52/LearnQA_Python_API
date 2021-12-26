import requests

respons = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(respons.text)
print('*'*30)

respons_h = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(respons_h.text)
print('*'*30)

respons_g = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": "GET"})
print(respons_g.text)
print('*'*30)

respons_p = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": "POST"})
print(respons_p.text)
print('*'*30)

method_list = ['GET', 'POST', 'PUT', 'DELETE' 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

for i in range(len(method_list)):
    respons_i = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={"method": method_list[i]})
    print(respons_i.text)
print('*'*30)

for i in range(len(method_list)):
    respons_i = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={"method": method_list[i]})
    print(respons_i.text)
print('*'*30)

for i in range(len(method_list)):
    respons_i = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type',
                             data={"method": method_list[i]})
    print(respons_i.text)
print('*'*30)

for i in range(len(method_list)):
    respons_i = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                data={"method": method_list[i]})
    print(respons_i.text)
print('*'*30)

for i in range(len(method_list)):
    respons_i = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type',
                                data={"method": method_list[i]})
    print(respons_i.text)
print('*'*30)
