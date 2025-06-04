import requests
from data import *


class OrderMethods:

    @staticmethod
    def create_order(ingredients, access_token=''):
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}", data=ingredients,
                                 headers={'Authorization': access_token})
        return response

    @staticmethod
    def get_current_user_orders_with_authorization(access_token):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}", headers={'Authorization': access_token})
        return response

    @staticmethod
    def get_current_user_orders_without_authorization():
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}")
        return response

    @staticmethod
    def get_ingredients_list():
        response = requests.get(f"{Urls.BASE_URL}{Urls.INGREDIENTS_LIST_URL}")
        return response
