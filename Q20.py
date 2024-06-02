#Lowest Revenue Generated Restaurants

import pandas as pd

result = doordash_delivery[doordash_delivery['customer_placed_order_datetime'].between('2020-05-01', '2020-05-31')].groupby("restaurant_id")["order_total"].sum().to_frame('total_order').reset_index()  
result['ntile'] = pd.qcut(result['total_order'],q=50, labels=range(1, 50), duplicates = 'drop').values.tolist()
result = result[result['ntile']==1][['restaurant_id','total_order']].sort_values('total_order', ascending=False)
