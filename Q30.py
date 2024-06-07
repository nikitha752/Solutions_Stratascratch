import pandas as pd


df = pd.merge(ms_user_dimension, ms_acc_dimension, left_on='acc_id', right_on='acc_id', how='left')
res = pd.merge(ms_download_facts, df, left_on='user_id', right_on='user_id', how='left')

res = res.groupby(['date', 'paying_customer'])['downloads'].sum().reset_index()

res['no'] = res[res['paying_customer']=='no']['downloads']
res['yes'] = res.loc[res['paying_customer']=='yes', 'downloads']

result_df = res.groupby('date').agg({'no': 'sum', 'yes': 'sum'}).reset_index()
result_df = result_df[result_df['no']>result_df['yes']]

#or

import pandas as pd

df = pd.merge(ms_user_dimension, ms_acc_dimension, left_on='acc_id', right_on='acc_id', how='left')
res = pd.merge(ms_download_facts, df, left_on='user_id', right_on='user_id', how='left')

res = res.groupby(['date', 'paying_customer'])['downloads'].sum().reset_index()

final = res.pivot(index='date',columns='paying_customer',values='downloads').reset_index()
result = final.loc[final['no']>final['yes']].sort_values('date')

