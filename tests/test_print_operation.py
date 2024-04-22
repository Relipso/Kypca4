from src.utils import print_operation
import datetime
# Тесты проверяющие вывод данных


def test_print_operation_one(capsys):
    formatted_operation = {
        "date": datetime.date(2010, 8, 15),
        "description": "Перевод организации",
        "from_mask": "Maestro 7810 84** **** 5568",
        "to_mask": "Счет **2869",
        "amount": "30153.72",
        "currency": "руб"
    }

    expected_output = ("15.08.2010 Перевод организации\n"
                       "Maestro 7810 84** **** 5568 -> Счет **2869\n"
                       "30153.72 руб\n\n")

    print_operation(formatted_operation)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_operation_two(capsys):
    formatted_operation = {
        "date": datetime.date(2010, 8, 15),
        "description": "Перевод организации",
        "from_mask": "",
        "to_mask": "Счет **2869",
        "amount": "30153.72",
        "currency": "руб"
    }

    expected_output = ("15.08.2010 Перевод организации\n"
                       "Счет **2869\n"
                       "30153.72 руб\n\n")

    print_operation(formatted_operation)
    captured = capsys.readouterr()
    assert captured.out == expected_output
