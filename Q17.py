#Find the variance and the standard deviation of scores that have grade A

import pandas as pd
import numpy as np

df =los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['grade']=='A']
df['sub']= 0
df['mean']= np.mean(df['score'])

def fun(row):
    row['sub']= (row['score']-row['mean'])**2
    return row
df = df.apply(fun, axis=1)
variance= np.mean(df['sub'])
std= np.sqrt(variance)
pd.DataFrame({'variance': variance, 'std': std}, index=[0])

#or

import pandas as pd
import numpy as np

df =los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['grade']=='A']
main = df[['score']]
main['mean']= np.mean(df['score'])
main['x']= (main['score']-main['mean'])**2
main['variance']= np.mean(main['x'])
main['std']= np.sqrt(main['variance'])
