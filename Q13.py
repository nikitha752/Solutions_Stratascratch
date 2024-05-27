#Find the genre of the person with the most number of oscar winnings

import pandas as pd

df=oscar_nominees[oscar_nominees['winner']]
df=df.groupby('nominee').size().to_frame('count').reset_index()

res = pd.merge(df,nominee_information, left_on='nominee', right_on='name', how='left')


res.groupby(['nominee','top_genre']).size().to_frame('count').reset_index().sort_values(['count','nominee'], ascending= [False,True]).head(1)[['top_genre']]
