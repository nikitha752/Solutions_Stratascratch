#output's dataframe but result shows series

import pandas as pd
import numpy as np

df = uber_advertising[uber_advertising['customers_acquired']>1500]
res = df.groupby('advertising_channel')['money_spent'].agg(max).reset_index().sort_values('money_spent').head(1)
res['advertising_channel']
