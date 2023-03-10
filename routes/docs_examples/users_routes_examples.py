import schemas.docs_examples.users_schemas_examples as users_schemas_examples

info_current_user_responses_examples = {
    200: {
        "description": "Успешное получение информации пользователя",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Полная информация пользователя",
                        "description": "Пример ответа при успешном получении информации пользователя",
                        "value": users_schemas_examples.user_full_examples['default']['value']
                    }
                }
            }
        }
    },
}
