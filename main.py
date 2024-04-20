from src.utils import load_operations, process_operation, print_operation

# Здесь загружаем операции, обрабатываем каждую операцию с помощью функции process_operation(),
# а затем выводим отформатированную информацию по операции с помощью функции print_operation().


operations = load_operations()

for operation in operations:
    formatted_operation = process_operation(operation)
    print_operation(formatted_operation)
