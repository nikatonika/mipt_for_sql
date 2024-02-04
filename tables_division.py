import pandas as pd

transactions = pd.read_csv('data/transaction.csv', sep=';')
customers = pd.read_csv('data/customer.csv', sep=';')

# Разделяю таблицу трансзакций на Продукты и Трансзакции
products = transactions[['product_id', 'brand', 'product_line', 'product_class', 'product_size', 'list_price', 'standard_cost']].copy()
products.drop_duplicates(subset='product_id', inplace=True)
customers = customers[['customer_id', 'first_name', 'last_name', 'gender', 'DOB', 'job_title', 'job_industry_category', 'wealth_segment', 'deceased_indicator', 'owns_car', 'address', 'postcode', 'state', 'country', 'property_valuation']].copy()
customers.drop_duplicates(subset='customer_id', inplace=True)

# Нормализую поле Пол
gender_mapping = {'Female': 'F', 'Male': 'M', 'U': 'Unknown'}
customers['gender'] = customers['gender'].replace(gender_mapping)

# Нормализую даты
transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'], format='%d/%m/%y')
customers['DOB'] = pd.to_datetime(customers['DOB'], format='%Y-%m-%d')

# Сохраняю таблицы
transactions.to_csv('data/normalized_transactions.csv', index=False)
products.to_csv('data/normalized_products.csv', index=False)
customers.to_csv('data/normalized_customers.csv', index=False)
