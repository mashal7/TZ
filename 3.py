import requests


def check_status_code(status_code, expected_status_code):
    '''Функция для проверки статус-кода'''

    assert status_code == expected_status_code, f'Ошибка! Статус-код {status_code}, неверный'
    print(f'Успешно! Статус код = {status_code}')

def check_body_value(response, field_name, expected_value):
    '''Функция для проверки наличия и  значения полей в ответе запроса'''

    response_json = response.json()
    assert field_name in response_json, f'Ошибка! В теле ответа нет поля {field_name}'
    field_value = response_json.get(field_name)
    assert field_value == expected_value, f'ОШИБКА, Значение поля "{field_name}" неверное'
    print(f'Значение поля "{field_name}" верное!')



# -------создание нового питомца методом post (id=5, name='Барсик')------------
base_url = 'https://petstore.swagger.io/v2'
id, name = 5, 'Барсик'

print('-------Создание нового питомца-------')
post_resource = '/pet'
post_url = f'{base_url}{post_resource}'
print(f'url: {post_url}')
body = {
    "id": id,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": name,
    "photoUrls": [
       "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

try:
    # отправка запроса
    response_post = requests.post(post_url, json=body)
    print(f'Тело ответа: {response_post.text}')

    # проверка статус-кода
    check_status_code(response_post.status_code, 200)

    # проверка наличия полей и их значений в теле ответа
    check_body_value(response_post, 'id', id)
    check_body_value(response_post, 'name', name)
    check_body_value(response_post, 'photoUrls', ['string'])
    print('-------Запрос выполнен успешно-------')

except requests.exceptions.RequestException as err:
    print(f'Ошибка запроса: {err}')


# -------------------Проверим наличие нового питомца: отправка метода get по id------------------------------
print('\n-------Проверка создания нового питомца-------')
get_resource = f'/pet/{id}'
get_url = f'{base_url}{get_resource}'
print(f'url: {get_url}')

try:
    # отправка запроса
    response_get = requests.get(get_url)
    print(f'Тело ответа: {response_get.text}')

    # проверка статус-кода
    check_status_code(response_get.status_code, 200)

    # проверка наличия полей и их значений в теле ответа
    check_body_value(response_get, 'id', id)
    check_body_value(response_get, 'name', name)
    print('-------Запрос выполнен успешно-------')

except requests.exceptions.RequestException as err:
    print(f'Ошибка запроса: {err}')


