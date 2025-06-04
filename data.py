class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    USER_CREATE_URL = '/auth/register'
    USER_LOGIN_URL = '/auth/login'
    USER_DATA_UPDATE_URL = '/auth/user'
    CREATE_ORDER_URL = '/orders'
    GET_USER_ORDERS_URL = '/orders'
    GET_LIST_INGREDIENTS_URL = '/ingredients'

payload = {
"email": "test-data@yandex.ru",
"password": "password",
"name": "Username"
}

ingredients = {
"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
}

class Users:
    USER_CREATED = 200, {"success": true,"user": {"email": "ann1@mail.ru","name": "Anna"
    },
    "accessToken": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4M2ZlNjYxOWVkMjgwMDAxYjYwOWEzMCIsImlhdCI6MTc0OTAxODIwOSwiZXhwIjoxNzQ5MDE5NDA5fQ.E8FFu5P4oYcEshKk604ih158cBBd80EwyRTsSTPVWQM",
    "refreshToken": "01bb921c4c07e01684fcfc7f5fc751a882a5666a340700439f256a09194513cf2b3ab734e03ee7ec"
}
    SAME_LOGIN = 403, {"success": false,"message": "User already exists"}#в ответе в постмане false без кавычек
    MISSING_FIELD = 403, {"success": false,"message": "Email, password and name are required fields"}
    USER_EXISTS = 403, {"success": true,"accessToken": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4M2ZlYTI4OWVkMjgwMDAxYjYwOWEzMiIsImlhdCI6MTc0OTAxOTI2MSwiZXhwIjoxNzQ5MDIwNDYxfQ.hrUbZgPIqTVcQsO8MdDknOaesjn5jypf0oFOWSjOr4c",
    "refreshToken": "b79f51257d95513b13201e005270fc3628189a8acaefcf9136e773c548353bc4d20c1423f7e6b4e5",
    "user": {
        "email": "tester24@yandex.ru",
        "name": "Username"
    }
}
    WRONG_PASSWORD = 401, {"success": false,"message": "email or password are incorrect"}
    WRONG_LOGIN = 401, {"success": false,"message": "email or password are incorrect"}
    BEARER_AUTHORIZATION_ANSWER = 200, {"success": true,"user": {"email": "tester24@yandex.ru","name": "Username"}}
    CHANGE_USER_DATA = 200, {"success": true,"user": {"email": "tester24@yandex.ru","name": "user"}}
    CHANGE_USER_DATA_NO_AUTH = 401, {"success": false,"message": "You should be authorised"}

class Orders:
    ORDER_CREATED = 200, {"success": true,"name": "Space традиционный-галактический бургер","order": {"number": 6221}}
    ORDER_WITH_INGREDIENTS = 200, {"success": true,"name": "Space традиционный-галактический бургер","order": {"number": 6221}}
    NO_INGREDIENTS_ORDER = 400, {"success": false,"message": "Ingredient ids must be provided"}
    WRONG_HASH = 500