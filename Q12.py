#Find all businesses whose lowest and highest inspection scores are different

import pandas as pd

df=sf_restaurant_health_violations.groupby('business_name').inspection_score.agg([min,max]).reset_index()
df=df[df['min']!=df['max']]
df.columns=['business_name','min_score','max_score']
df.dropna()
