import requests
from data import *
class OrderMethods:

    #
    def create_order(self):
        response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE_ORDER_URL}", ingredients)
        return response


    def get_current_user_orders_with_authorization(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}, headers={'Authorization': 'accessToken'}")
        return response

    def get_current_user_orders_without_authorization(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_USER_ORDERS_URL}")
        return response

    def get_ingredients_list(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_LIST_INGREDIENTS_URL}")
        return response

