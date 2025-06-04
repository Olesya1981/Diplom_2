import requests
from data import *


class User_methods:

    # Создаем уникального пользователя
    @staticmethod
    def create_unique_user(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_CREATE_URL}", payload)
        return response

    # Авторизуемся с логином и паролем
    @staticmethod
    def login_user(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", payload)
        return response

    # Изменяем данные пользователя
    @staticmethod
    def change_user_data(access_token, payload):
        response = requests.patch(f"{Urls.BASE_URL}{Urls.USER_DATA_UPDATE_URL}",
                                  headers={'Authorization': access_token}, data=payload)
        return response
