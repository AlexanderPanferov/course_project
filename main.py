from utils.utils import load_operation, selection_by_keys, completed_operation, sort_date, last_operation, \
    format_operation

if __name__ == '__main__':

    filename = "operations.json"

    operation = load_operation(filename)
    full_operations = selection_by_keys(operation)
    executed = completed_operation(full_operations)
    date_operation = sort_date(executed)
    recent_operations = last_operation(executed, date_operation)
    edited_operation = format_operation(recent_operations)

    # Цикл вывода последних 5 операций
    for item in edited_operation:
        print()
        print(f'{item["date"]} {item["description"]}')
        print(f'{item["from"]} -> {item["to"]}')
        print(f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')
