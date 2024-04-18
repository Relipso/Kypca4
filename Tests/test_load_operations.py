import pytest
from src.main import load_operations


def test_load_operations_one():
    """Тест, проверяющий возвращает ли функция пять операций"""
    operations = load_operations()
    assert len(operations) == 5


def test_load_operations_two():
    """Тест, который проверяет статус операции"""
    operations = load_operations()
    for operation in operations:
        assert operation["state"] == "EXECUTED"


def test_load_operations_three():
    """Тест, который проверяет сортировку операций по самой новой дате"""
    operations = load_operations()
    dates = [operation["date"] for operation in operations]
    assert dates == sorted(dates, reverse=True)
