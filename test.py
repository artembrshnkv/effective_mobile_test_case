import unittest

from wallet import Wallet
from utils import table_exists


class TestWallet(unittest.TestCase):
    test_data = ['2024-05-02,Расход,1500,Покупка продуктов\n']

    def setUp(self) -> None:
        self.wallet = Wallet('test-db')

    def test_select(self):
        self.assertEqual(
            self.wallet.select_where_date('2024-05-02'),
            self.test_data
        )
        self.assertEqual(
            self.wallet.select_where_category('Расход'),
            self.test_data
        )
        self.assertEqual(self.wallet.select_where_amount(1500), self.test_data)

    def test_table_exists(self):
        self.assertEqual(table_exists('test-db'), True)
        self.assertEqual(table_exists('testtesttest-db'), False)


if __name__ == '__main__':
    unittest.main()
