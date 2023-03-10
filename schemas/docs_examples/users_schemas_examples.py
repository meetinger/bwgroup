user_in_examples = {
    "default": {
        "summary": "Данные пользователя",
        "description": "Пример пользовательских данных",
        "value": {
            "username": "example_username",
            "name": "Example Name",
            "balance": "39.99",
            "password": "a_very_strong_password"
        }
    }
}
user_full_examples = {
    "default": {
        "summary": "Данные пользователя",
        "description": "Пример полных пользовательских данных",
        "value": {'id': 1} | {key: value for key, value in
                              user_in_examples['default']['value'].items() if key != 'password'}
    }
}

refresh_token_in_examples = {
    "default": {
        "summary": "Refresh токен",
        "description": "Пример refresh токена",
        "value": {'refresh_token': 'RefreshTokenStr'}
    }
}
