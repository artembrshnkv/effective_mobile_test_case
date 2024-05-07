from os import path
from constants import category_types, table_rows_order


def table_exists(filename: str) -> bool:
    return path.exists(f'{filename}.csv')


def normalize_data(data: list) -> list:
    normalized_data = []
    for item in data:
        try:
            normalized_data.append(str(item))
        except():
            raise TypeError('Invalid data type')

    return normalized_data


def formate_line(data: list) -> str:
    line_data = normalize_data(data)
    return ','.join(line_data)


def calc_sum_by_the_category(table_name: str,
                             category_type: str | None = None) -> int:
    debit = 0
    credit = 0
    with open(f'{table_name}.csv', 'r') as file:
        for line in file:
            items = line.split(',')
            operation_category = items[table_rows_order['category']]
            amount = items[table_rows_order['amount']]

            if operation_category is category_types['debit']:
                debit += int(amount)
            elif operation_category is category_types['credit']:
                credit -= int(amount)

    if not category_type:
        return debit + credit
    elif category_type is category_types['debit']:
        return debit
    elif category_type is category_types['credit']:
        return credit


def select_where(table_name: str,
                 search_field: str,
                 search_value: str) -> list:
    query = []
    with open(f'{table_name}.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if line.split(',')[table_rows_order[search_field]] == search_value:
                query.append(line)

    return query
