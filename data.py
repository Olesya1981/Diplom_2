class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    USER_CREATE_URL = '/auth/register'
    USER_LOGIN_URL = '/auth/login'
    USER_DATA_UPDATE_URL = '/auth/user'
    CREATE_ORDER_URL = '/orders'
    GET_USER_ORDERS_URL = '/orders'
    GET_LIST_INGREDIENTS_URL = '/ingredients'

existing_payload = {'email': 'gena@krokodil.com', 'password': '4pmlrXgw$ap', 'name': 'Gennady'}

ingredients = {
"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
}

class Users:
    SUCCESS = 200, True
    SAME_LOGIN = 403, {"success": False,"message": "User already exists"}
    MISSING_FIELD = 403, {"success": False,"message":"Email, password and name are required fields"}
    WRONG_PASSWORD = 401, {"success": False,"message": "email or password are incorrect"}
    WRONG_LOGIN = 401, {"success": False,"message": "email or password are incorrect"}
    BEARER_AUTHORIZATION_ANSWER = 200, {"success": True, "user": {"email": "tester24@yandex.ru","name": "Username"}}
    CHANGE_USER_DATA = 200, {"success": True,"user": {"email": "tester24@yandex.ru","name": "user"}}
    CHANGE_USER_DATA_NO_AUTH = 401, {"success": False,"message": "You should be authorised"}

class Orders:
    ORDER_CREATED = 200, {"success": 'true',"name": "Space традиционный-галактический бургер","order": {"number": 6221}}
    ORDER_WITH_INGREDIENTS = 200, {"success": 'true',"name": "Space традиционный-галактический бургер","order": {"number": 6221}}
    NO_INGREDIENTS_ORDER = 400, {"success": 'false',"message": "Ingredient ids must be provided"}
    WRONG_HASH = 500