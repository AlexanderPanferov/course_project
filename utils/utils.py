import json
from datetime import datetime


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


def sort_date(executed):
    """

    :param executed: список с выполненными опереациями
    :return: отсортированный список содержащий последнии 5 дат
    """
    date = []
    for item in executed:
        date.append(item['date'])
    date.sort(reverse=True)
    if len(date) < 5:
        return date
    else:
        date_sort = date[:5]
    return date_sort


def last_operation(executed, date_operation):
    """

    :param executed: список с выполненными опереациями
    :param date_operation: отсортированный список содержащий последнии 5 дат
    :return: отсортированный список содержащий последнии 5 операций
    """
    last_list = []
    for item in date_operation:
        for i in executed:
            if item in i['date']:
                last_list.append(i)
    return last_list


def format_str(str_f):
    """

    :param str_f: строку с данными
    :return: список содержащий буквы отдельно от цифры

    сортирует строку на цифры и буквы
    """
    text = ''
    digits = ''
    list_str = []
    for item in str_f:
        if item.isalpha() or item.isspace():
            text += item
        elif item.isdigit():
            digits += item
    list_str.append(text)
    list_str.append(digits)
    return list_str


def format_operation(formated):
    """

    :param formated: отсортированный список содержащий последнии 5 операций
    :return: отредактированный список содержащий последнии 5 операций

    форматирует дату
    поля from,to
    """
    formatted_list = []
    for item in formated:
        date = datetime.strptime(item["date"], '%Y-%m-%dT%H:%M:%S.%f')
        item["date"] = date.strftime('%d.%m.%Y')
        send = format_str(item['from'])
        item['from'] = f'{send[0]}{send[1][:4]} {send[1][4:6]}** **** {send[1][-4:]}'
        accept = format_str(item['to'])
        item["to"] = f'{accept[0]}**{accept[1][-4:]}'
        formatted_list.append(item)
    return formatted_list
