import pandas as pd
import numpy as np

df= pd.merge(instacart_reviews, instacart_stores, left_on='store_id', right_on='id', how='left')
df= df[df['opening_date'].between('2021-07-01','2021-12-31')]

def func(row):
    if row.score>=5:
        return 0
    else:
        return 1
df['review'] = df.apply(func, axis=1)

df = df.groupby('name').review.agg(["sum","count"]).reset_index()
df['neg_percentage'] = df['sum']/df['count']
df['negative_positive_ratio'] = df['sum']/(df['count']-df['sum'])

res = df[df['neg_percentage']>0.2][['name','negative_positive_ratio']]
