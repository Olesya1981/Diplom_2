import allure
from data import *
class TestOrders:
#создание заказа:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self):
        #assert (response.status_code, response.text) == Orders.ORDER_CREATED

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        ##assert (response.status_code, response.text) == Orders.ORDER_CREATED

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        # assert (response.status_code, response.text) == Orders.ORDER_CREATED

    @allure.title(" Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        #assert(response.status_code, response.text) = Orders.NO_INGREDIENTS_ORDER


    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_create_order_with_wrong_imgredients_hash(self):
        #assert(response.status_code, response.text) = Orders.WRONG_HASH

#Получение заказов конкретного пользователя

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_user_orders_user_is_authorized(self):

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_user_orders_user_is_not_authorized(self):

