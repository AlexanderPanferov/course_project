import json


def load_operation(filename):
    """

    :param filename: файл json
    :return: список с банковскими операциями
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operation = json.load(file)
    return operation


def selection_by_keys(operation):
    """

    :param operation: список с банковскими операциями
    :return: фильтрованный список

    Проверяет наличие ключей в словаре
    """
    filtered_list = []
    keys_to_check = ['state', 'date', 'description', 'from', 'to']
    for item in operation:
        if all(key in item.keys() for key in keys_to_check):
            filtered_list.append(item)
    return filtered_list


def completed_operation(full_operations):
    """

    :param full_operations: список операций с полными данными
    :return:список с выполненными опереациями(EXECUTED)
    """
    exe_list = []
    for item in full_operations:
        if item['state'] == 'EXECUTED':
            exe_list.append(item)
    return exe_list
