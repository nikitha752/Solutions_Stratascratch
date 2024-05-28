#Year Over Year Churn

import pandas as pd

lyft_drivers['year_left']= lyft_drivers['end_date'].dt.year
df = lyft_drivers.groupby('year_left').size().to_frame('total_churn').reset_index()

df['prev_year_churn']= df.total_churn.shift(1).fillna(0)

def change(row):
    if (row.total_churn>row.prev_year_churn):
        return 'increase'
    elif(row.total_churn==row.prev_year_churn):
        return 'no change'
    else:
        return 'decrease'
    
df['inc/dec']= df.apply(change, axis=1)
df
