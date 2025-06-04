import requests
from data import *


class Users:

    # Создаем уникального пользователя
    def create_unique_user(self):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_CREATE_URL}", payload)
        yield response


    # Авторизуемся с логином и паролем
    def login_user(self):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", email, password)
        return response

    # Изменяем данные пользователя
    def change_user_data(self):
        response = requests.patch(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", headers={'Authorization': 'accessToken'})
        return response
