from schemas.docs_examples import transactions_schemas_examples

current_user_transactions_list = {
    200: {
        "description": "Успешное получение списка последних транзакций пользователя",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Список транзакций",
                        "description": "Пример списка транзакций",
                        "value": [transactions_schemas_examples.transaction_out_examples['default']['value']]
                    }
                }
            }
        }
    },
}

create_transaction = {
    200: {
        "description": "Успешное создание транзакции",
        "content": {
            "application/json": {
                "examples": {
                    "default": {
                        "summary": "Транзакция",
                        "description": "Пример транзакции",
                        "value": transactions_schemas_examples.transaction_out_examples['default']['value']
                    }
                }
            }
        }
    },
}
