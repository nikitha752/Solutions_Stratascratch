#Monthly Percentage Difference

import pandas as pd
import numpy as np
from datetime import datetime
pd.options.display.float_format = "{:,.2f}".format

sf_transactions['created_at'] = sf_transactions['created_at'].apply(pd.to_datetime)
sf_transactions['year_month'] = pd.to_datetime(sf_transactions['created_at']).dt.to_period('M')
df = sf_transactions.groupby('year_month')['value'].sum().reset_index(name='monthly_revenue').sort_values('year_month')
df['prev_value'] = df['monthly_revenue'].shift(1)
df['revenue_diff_pct'] = round(((df['monthly_revenue'] - df['prev_value'])/df['prev_value'])*100, 2)
result = df[['year_month','revenue_diff_pct']].fillna('')
