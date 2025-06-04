class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    USER_CREATE_URL = '/auth/register'
    USER_LOGIN_URL = '/auth/login'
    USER_DATA_UPDATE_URL = '/auth/user'
    CREATE_ORDER_URL = '/orders'
    GET_USER_ORDERS_URL = '/orders'
    INGREDIENTS_LIST_URL = '/ingredients'

EXISTING_PAYLOAD = {'email': 'gena@krokodil.com', 'password': '4pmlrXgw$ap', 'name': 'Gennady'}
WRONG_HASH = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}
NUMBER_LIST = [236410, 236411, 236413, 236428, 236429, 236431, 236435, 236436, 236438, 236440, 236441, 236442]

class Users:
    SUCCESS = 200, True
    SAME_LOGIN = 403, {"success": False,"message": "User already exists"}
    MISSING_FIELD = 403, {"success": False,"message":"Email, password and name are required fields"}
    WRONG_PASSWORD = 401, {"success": False,"message": "email or password are incorrect"}
    WRONG_LOGIN = 401, {"success": False,"message": "email or password are incorrect"}
    CHANGE_USER_DATA_NO_AUTH = 401, {"success": False,"message": "You should be authorised"}

class Orders:
    ORDER_CREATED = 200, True
    NO_INGREDIENTS_ORDER = 400, {"success": False,"message": "Ingredient ids must be provided"}
    WRONG_HASH = 400, {'success': False, 'message': 'One or more ids provided are incorrect'}
    GET_ORDERS_WITHOUT_AUTHORIZATION = 401, {'success': False, 'message': 'You should be authorised'}