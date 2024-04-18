import json
from datetime import datetime


def load_operations():
    """В этой функции идёт вывод операций, затем идет проверка операции по её статусу,
    в конце происходит сортировка по дате"""
    with open("D:/Python/Kypca4/operations.json", "r", encoding="utf-8") as file:
        operations = json.load(file)

    executed_operations = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    sorted_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)[:5]

    return sorted_operations


def process_operation(operation):
    """В этой функции идет преобразование данных, для их дальнейшего вывода"""
    date = operation["date"][:10]
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["name"]
    description = operation["description"]
    from_operations = operation.get("from", "")
    to_operations = operation["to"]

    format_date = datetime.strptime(date, "%Y-%m-%d")

    from_mask = masked_operation(from_operations)
    to_mask = masked_operation(to_operations)

    return {
        "date": format_date,
        "description": description,
        "from_mask": from_mask,
        "to_mask": to_mask,
        "amount": amount,
        "currency": currency
    }


def masked_operation(from_and_to):
    """В этой функции идёт маскировка номера счёта, откуда и куда"""
    if "Счет" in from_and_to:
        to_split = from_and_to.split(" ")
        to_operation = to_split[-1]
        mask_operation = len(to_operation[:-4]) * "*" + to_operation[-4:]
        return "Счет " + mask_operation
    else:
        from_split = from_and_to.rsplit(" ", 1)
        from_op = from_split[-1]
        mask_operation = from_op[0:4] + " " + from_op[4:6] + " " + len(from_op[6:-4]) * "*" + " " + from_op[-4:]
        return from_split[0] + " " + mask_operation


def print_operation(formatted_operation):
    """Здесь идёт вывод данных по операции, с замаскированным номером и измененной датой"""
    print(f"{formatted_operation["date"].strftime("%d.%m.%Y")} {formatted_operation["description"]}")
    print(f"{formatted_operation["from_mask"]} -> {formatted_operation["to_mask"]}")
    print(f"{formatted_operation["amount"]} {formatted_operation["currency"]}")
    print()

# Здесь загружаем операции, обрабатываем каждую операцию с помощью функции process_operation(),
# а затем выводим отформатированную информацию по операции с помощью функции print_operation().


operations = load_operations()

for operation in operations:
    formatted_operation = process_operation(operation)
    print_operation(formatted_operation)