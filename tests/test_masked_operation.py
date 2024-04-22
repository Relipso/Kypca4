import pytest
from src.utils import masked_operation

# Тесты проверяющие как будет маскироваться счёт и его номер


def test_masked_operation_one():
    assert masked_operation("Счет 1234567891011121") == "Счет **1121"


def test_masked_operation_two():
    assert masked_operation("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_masked_operation_three():
    assert masked_operation("Два слова 1234567659101121") == "Два слова 1234 56** **** 1121"
