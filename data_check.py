import pandas as pd

transactions = pd.read_csv('data/transaction.csv', sep=';')
customers = pd.read_csv('data/customer.csv', sep=';')

# Проверяю данные на целостность
unique_customers_in_transactions = set(transactions['customer_id'].unique())
unique_customers = set(customers['customer_id'].unique())
missing_customers = unique_customers_in_transactions - unique_customers

print(f"Количество отсутствующих customer_id: {len(missing_customers)}")
print(f"Отсутствующие customer_id: {missing_customers}")

missing_transactions = transactions[transactions['customer_id'].isin(missing_customers)]
print(missing_transactions)

# Удаляю трансзакции с несуществующими кастомерами
transactions_cleaned = transactions[~transactions['customer_id'].isin(missing_customers)]

# Сохраненяю новый файл
transactions_cleaned.to_csv('data/cleaned_transactions.csv', sep=',', index=False)
