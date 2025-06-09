import allure
import requests
from data import *


class UserMethods:

    @staticmethod
    @allure.step("Создаём уникального пользователя")
    def create_unique_user(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_CREATE_URL}", payload)
        return response

    @staticmethod
    @allure.step("Авторизуемся с логином и паролем")
    def login_user(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.USER_LOGIN_URL}", payload)
        return response

    @staticmethod
    @allure.step("Меняем данные пользователя")
    def change_user_data(access_token, payload):
        response = requests.patch(f"{Urls.BASE_URL}{Urls.USER_DATA_UPDATE_URL}",
                                  headers={'Authorization': access_token}, data=payload)
        return response
