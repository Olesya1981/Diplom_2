import requests
from data import *
import allure


class OrderMethods:

    @staticmethod
    @allure.step("Создаем заказ")
    def create_order(ingredients, access_token=''):
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}", data=ingredients,
                                 headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step("Получение заказов конкретного авторизованного пользователя")
    def get_current_user_orders_with_authorization(access_token):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}", headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.step("Получение заказов конкретного пользователя без авторизации")
    def get_current_user_orders_without_authorization():
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}")
        return response

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def get_ingredients_list():
        response = requests.get(f"{Urls.BASE_URL}{Urls.INGREDIENTS_LIST_URL}")
        return response
