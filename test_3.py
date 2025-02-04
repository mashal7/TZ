import requests
import pytest

# данные для теста
base_url = 'https://petstore.swagger.io/v2'
id, name = 5, 'Барсик'

# Проверки
def check_status_code(status_code, expected_status_code):
    '''Функция для проверки статус-кода'''

    assert status_code == expected_status_code, f'Ошибка! Статус-код {status_code}, неверный'
    print(f'Успешно! Статус код = {status_code}')

def check_body_value(response, field_name, expected_value):
    '''Функция для проверки наличия и значения полей в ответе запроса'''

    response_json = response.json()
    assert field_name in response_json, f'Ошибка! В теле ответа нет поля {field_name}'
    field_value = response_json.get(field_name)
    assert field_value == expected_value, f'ОШИБКА, Значение поля "{field_name}" неверное'
    print(f'Значение поля "{field_name}" верное!')

def check_header_value(response, header_name, expected_value=None):
    '''Функция для проверки наличия и значения заголовков в ответе'''
    assert header_name in response.headers, f'Ошибка! Заголовок {header_name} отсутствует'
    header_value = response.headers.get(header_name)
    assert header_value == expected_value, f'ОШИБКА, Значение заголовка "{header_name}" неверное'
    print(f'Значение заголовка "{header_name}" верное!')


def post_pet(base_url, id, name):
    '''Метод post для создания питомца'''
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
        response = requests.post(post_url, json=body)
        return response
    except requests.exceptions.RequestException as err:
        print(f'Ошибка запроса: {err}')


def get_pet(base_url, id):
    '''Метод get для получения информации о  питомце'''

    get_resource = f'/pet/{id}'
    get_url = f'{base_url}{get_resource}'
    print(f'url: {get_url}')

    try:
        response = requests.get(get_url)
        return response
    except requests.exceptions.RequestException as err:
        print(f'Ошибка запроса: {err}')


def test_create_pet():
    '''Проверка наличия нового питомца: отправка метода get по id'''

    print('\n-------Создание нового питомца-------')
    # отправка запроса
    response_post = post_pet(base_url, id, name)
    print(f'Тело ответа: {response_post.text}')

    # проверка статус-кода
    check_status_code(response_post.status_code, 200)

    # проверка наличия полей и их значений в теле ответа
    expected_fields = {'id': id, 'name': name, 'photoUrls': ['string']}
    for field_name, expected_value in expected_fields.items():
        check_body_value(response_post, field_name, expected_value)

    # проверка заголовков (например, Content-Type)
    check_header_value(response_post, 'Content-Type', 'application/json')

    print('-------Запрос выполнен успешно-------')

def test_get_pet():
    '''Создание нового питомца методом post (id=5, name='Барсик')'''

    print('\n-------Проверка создания нового питомца-------')
    # отправка запроса
    response_get = get_pet(base_url, id)

    # проверка статус-кода
    check_status_code(response_get.status_code, 200)

    # проверка наличия полей и их значений в теле ответа
    check_body_value(response_get, 'id', id)
    check_body_value(response_get, 'name', name)

    # проверка заголовков (например, Content-Type)
    check_header_value(response_get, 'Content-Type', 'application/json')

    print('-------Запрос выполнен успешно-------')


