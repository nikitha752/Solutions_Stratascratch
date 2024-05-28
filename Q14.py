import pandas as pd

df = pd.merge(employee, bonus, left_on='id', right_on='worker_ref_id', how='left')

df['has_bonus']=df.bonus_amount.notnull().astype(int)
result = df.groupby('has_bonus').id.nunique()
