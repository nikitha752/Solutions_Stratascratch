import pandas as pd

df = facebook_friends[['user2', 'user1']]
df = df.rename(columns={'user2': 'user1', 'user1': 'user2'})
res = pd.concat([facebook_friends, df])
res = res.groupby('user1').size().to_frame('frnds').reset_index()
res['frnds'] = (res['frnds']/len(res))*100
res
