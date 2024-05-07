table_name = 'data'
# date_regexp = '^\d{4}-\d{2}-\d{2}$'
table_schema = ['date', 'category', 'amount', 'description']

table_rows_order = {
    'date': 0,
    'category': 1,
    'amount': 2,
    'description': 3,
}

category_types = {
    'debit': 'Доход',
    'credit': "Расход",
}
