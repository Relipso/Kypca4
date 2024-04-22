import pytest
from datetime import datetime
from src.utils import process_operation
# Тесты проверяющие преобразование данных


def test_process_operation_one():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    expected_output = {
        "date": datetime.strptime("2019-08-26", "%Y-%m-%d"),
        "description": "Перевод организации",
        "from_mask": "Maestro 1596 83** **** 5199",
        "to_mask": "Счет **9589",
        "amount": "31957.58",
        "currency": "руб."
    }

    assert process_operation(operation) == expected_output


def test_process_operation_two():
    operation = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 64686473678894779589"
    }

    expected_output = {
        "date": datetime.strptime("2019-08-26", "%Y-%m-%d"),
        "description": "Перевод организации",
        "from_mask": "",
        "to_mask": "Счет **9589",
        "amount": "31957.58",
        "currency": "руб."
    }

    assert process_operation(operation) == expected_output
