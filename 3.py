import requests


def check_status_code(status_code, expected_status_code):
    '''Функция для проверки статус-кода'''
    assert status_code == expected_status_code, f'Ошибка! Статус-код {status_code}, неверный'
    print(f'Успешно! Статус код = {status_code}')

def check_body_value(response, field_name, expected_value):
    '''Функция для проверки значения полей в ответе запроса'''
    check = response.json()
    assert field_name in check, f'Ошибка! В теле ответа нет поля {field_name}'
    field_value = check.get(field_name)
    assert field_value == expected_value, f'ОШИБКА, Значение поля "{field_name}" неверное'
    print(f'Значение поля "{field_name}" верное!')



# ----------------создание нового питомца и проверка наличия нового питомца по id (id=5, name='Барсик')---------------------
print('-------Создание нового питомца-------')
base_url = 'https://petstore.swagger.io/v2'
id, name = 5, 'Барсик'

# Создадим нового питомца
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

response_post = requests.post(post_url, json=body)
print(f'Тело ответа: {response_post.text}')

# проверка статус-кода
check_status_code(response_post.status_code, 200)

# проверка наличия полей и их значений в теле ответа
check_body_value(response_post, 'id', id)
check_body_value(response_post, 'name', name)


# -------------------Проверим наличие нового питомца: отправка метода get по id------------------------------
print('\n-------Проверка создания нового питомца-------')
get_resource = f'/pet/{id}'
get_url = f'{base_url}{get_resource}'
print(f'url: {get_url}')

response_get = requests.get(get_url)
print(f'Тело ответа: {response_get.text}')

# проверка статус-кода
check_status_code(response_get.status_code, 200)

# проверка наличия полей и их значений в теле ответа
check_body_value(response_get, 'id', id)
check_body_value(response_get, 'name', name)


