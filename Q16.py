#Find the top 5 least paid employees for each job title

import pandas as pd

sf_public_salaries['erank'] = sf_public_salaries.groupby('jobtitle').totalpaybenefits.rank(method='dense')
df= sf_public_salaries[sf_public_salaries['erank']<=5]

res= df[['employeename', 'jobtitle', 'totalpaybenefits']].sort_values(['jobtitle','totalpaybenefits'], ascending=[True,True])
