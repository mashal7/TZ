import requests




# Создадим нового заказа
def post_new_pet(id=5, name='Барсик'):
    post_resource = '/pet'
    post_url = f'{base_url}{post_resource}'
    body = {
        "id": {id},
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": {name},
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
    print(response_post.text)
    status_code = response_post.status_code
    assert status_code == 200, f'Ошибка! Статус-код {status_code} неверный'
    print(f'Статус-код {status_code} верный')


# Проверим его наличие в БД



# создание и проверка наличия нового питомца по id (id=5, name='Барсик')
base_url = 'https://petstore.swagger.io/v2'
post_new_pet(id=5, name='Барсик')

