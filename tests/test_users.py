from urllib import response

import allure
from methods.users_methods import *
from data import *
import requests


class TestUsers:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user_success(self):
        Users.create_unique_user()
        #assert (response.status_code)== Users.USER_CREATED

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_exists_user(self):
        #assert (response.status_code, response.text) == Users.SAME_LOGIN

    @allure.title("Создать пользователя, не заполнив одно из обязательных полей")
    def test_create_user_one_field_is_missing(self):
        #assert (response.status_code, response.text)== Users.MISSING_FIELD

    @allure.title("Логин под существующим пользователем логин и пароль")
    def test_login_exists_user_is_success(self):
        #assert(response.status_code, response_text)== Users.USER_EXISTS

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_wrong_login_and_wrong_password(self):
        #assert (response.status_code, response.text)==Users.WRONG_PASSWORD

    # Для обеих ситуаций нужно проверить, что любое поле можно изменить.
    # Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_user_data_with_authorization(self):
        #assert(response.status_code, response.text)== Users.CHANGE_USER_DATA

    @allure.title("Изменение данных пользователя без авторизации")
    def test_change_user_data_without_authorization(self):
        #assert((.status_code, response.text)== Users.CHANGE_USER_DATA_NO_AUTH
