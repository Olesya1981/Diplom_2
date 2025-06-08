import allure
from methods.order_methods import *
from methods.users_methods import *
from conftest import *


class TestOrders:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, create_new_user_and_delete):
        ingredients_list = OrderMethods.get_ingredients_list().json()['data']
        ingredients = []
        for _ in range(3):
            ingredients.append(choice(ingredients_list)['_id'])
        _, response = create_new_user_and_delete
        access_token = response.json()['accessToken']
        response = OrderMethods.create_order({'ingredients': ingredients}, access_token)
        assert (response.status_code, response.json()['success']) == Orders.ORDER_CREATED

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        ingredients_list = OrderMethods.get_ingredients_list().json()['data']
        ingredients = []
        for _ in range(3):
            ingredients.append(choice(ingredients_list)['_id'])
        response = OrderMethods.create_order({'ingredients': ingredients})
        assert (response.status_code, response.json()['success']) == Orders.ORDER_CREATED

    @allure.title(" Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = OrderMethods.create_order({})
        assert (response.status_code, response.json()) == Orders.NO_INGREDIENTS_ORDER

    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_create_order_with_wrong_ingredients_hash(self):
        response = OrderMethods.create_order(General.WRONG_HASH)
        assert (response.status_code, response.json()) == Orders.WRONG_HASH

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_user_orders_user_is_authorized(self):
        response = UserMethods.login_user(General.EXISTING_PAYLOAD)
        access_token = response.json()['accessToken']
        response = OrderMethods.get_current_user_orders_with_authorization(access_token)
        orders = response.json()['orders']
        number_list = [x['number'] for x in orders]
        assert number_list == General.NUMBER_LIST

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_user_orders_user_is_not_authorized(self):
        response = OrderMethods.get_current_user_orders_without_authorization()
        assert (response.status_code, response.json()) == Orders.GET_ORDERS_WITHOUT_AUTHORIZATION
