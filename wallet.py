from utils import table_exists, formate_line, \
    calc_sum_by_the_category, select_where
from constants import category_types, table_schema


class Wallet:
    def __init__(self, table_name: str):
        self.__table_name = table_name
        self.__init_table()

    def __init_table(self) -> None:
        if not table_exists(self.__table_name):
            first_line = formate_line(table_schema)
            with open(f'{self.__table_name}.csv', 'w',
                      encoding='utf-8') as file:
                file.write(f'{first_line}\n')

    def get_balance(self) -> int:
        return calc_sum_by_the_category(self.__table_name)

    def get_debit(self) -> int:
        return calc_sum_by_the_category(
            self.__table_name,
            category_types['debit']
        )

    def get_credit(self) -> int:
        return calc_sum_by_the_category(
            self.__table_name,
            category_types['credit']
        )

    def insert(self,
               date: str,
               category: str,
               amount: int,
               description: str) -> None:
        data = [date, category, str(amount), description]
        line = formate_line(data)
        with open(f'{self.__table_name}.csv', 'a',
                  encoding='utf-8') as file:
            file.write(f'{line}\n')

    def select_where_date(self, date: str) -> list:
        return select_where(self.__table_name, 'date', date)

    def select_where_category(self, category: str) -> list:
        return select_where(self.__table_name, 'category', category)

    def select_where_amount(self, amount: int) -> list:
        return select_where(self.__table_name, 'amount', str(amount))


if __name__ == '__main__':
    t = Wallet('db')
