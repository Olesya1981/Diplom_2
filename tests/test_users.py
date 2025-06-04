import allure
from methods.users_methods import *
from conftest import *
from helpers import *


class TestUsers:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user_success(self, create_new_user_and_delete):
        _, response = create_new_user_and_delete
        assert (response.status_code, response.json()['success']) == Users.SUCCESS

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_exists_user(self):
        payload = EXISTING_PAYLOAD
        response = UserMethods.create_unique_user(payload)
        assert (response.status_code, response.json()) == Users.SAME_LOGIN

    @allure.title("Создать пользователя, не заполнив одно из обязательных полей")
    @pytest.mark.parametrize("element", ['name', 'password', 'email'])
    def test_create_user_one_field_is_missing(self, element):
        payload = random_payload()
        del payload[element]
        response = UserMethods.create_unique_user(payload)
        assert (response.status_code, response.json())== Users.MISSING_FIELD

    @allure.title("Логин под существующим пользователем логин и пароль")
    def test_login_exists_user_is_success(self):
        payload = EXISTING_PAYLOAD
        response = UserMethods.login_user(payload)
        assert (response.status_code, response.json()['success']) == Users.SUCCESS

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_wrong_login_and_wrong_password(self):
        payload = EXISTING_PAYLOAD
        payload['password'] += 'z'
        response = UserMethods.login_user(payload)
        assert (response.status_code, response.json()) == Users.WRONG_PASSWORD

    # Для обеих ситуаций нужно проверить, что любое поле можно изменить.
    # Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("element", ['name', 'email'])
    def test_change_user_data_with_authorization(self, element, create_new_user_and_delete):
        payload, response = create_new_user_and_delete
        access_token = response.json()['accessToken']
        payload[element] = 'che@burashka.ru'
        response = UserMethods.change_user_data(access_token, payload)
        assert ((response.status_code, response.json()['success']) == Users.SUCCESS and
                response.json()['user'][element] == 'che@burashka.ru')

    @allure.title("Изменение данных пользователя без авторизации")
    @pytest.mark.parametrize("element", ['name', 'email'])
    def test_change_user_data_without_authorization(self, element):
        payload = EXISTING_PAYLOAD
        payload[element] = 'che@burashka.ru'
        response = UserMethods.change_user_data('', payload)
        assert(response.status_code, response.json())== Users.CHANGE_USER_DATA_NO_AUTH
