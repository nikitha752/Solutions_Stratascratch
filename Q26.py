import pandas as pd

df=  pd.merge(airbnb_units, airbnb_hosts, left_on='host_id', right_on='host_id', how='left')
df =  df[(df['unit_type']=='Apartment') & (df['age']<30)]
res = df.groupby('nationality')['unit_id'].nunique().to_frame('count').reset_index().sort_values('count')
