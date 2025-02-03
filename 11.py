from requests.auth import HTTPBasicAuth
import requests

base_url = 'https://restful-booker.herokuapp.com'
# Создадим нового питомца
post_resource = '/auth'
post_url = f'{base_url}{post_resource}'

# Данные для аутентификации
body = {'username': 'admin',
        'password': 'password123'}

response_post = requests.post(post_url, json=body)
print(response_post.text)

# проверка на статус-код
status_code = response_post.status_code
assert status_code == 200, f'Ошибка! Статус-код {status_code} неверный'
print(f'Статус-код {status_code} верный')

# проверка тела
assert status_code == 200, f'Ошибка! Статус-код {status_code} неверный'
print(f'Статус-код {status_code} верный')

