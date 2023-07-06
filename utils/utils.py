import json


def load_operation(filename):
    """

    :param filename: файл json
    :return: список с банковскими операциями
    """
    with open(filename, 'r', encoding='utf-8') as file:
        operation = json.load(file)
    return operation
