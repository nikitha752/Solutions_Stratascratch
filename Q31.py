import pandas as pd

df = pd.merge(excel_sql_transaction_data, excel_sql_inventory_data, left_on='product_id', right_on='product_id', how='left')
df = df.groupby(['product_id', 'product_name']).size().to_frame('size').reset_index().sort_values('product_id')
df = df[['product_name', 'size']]
