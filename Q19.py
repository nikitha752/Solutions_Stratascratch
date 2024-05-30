#First 50% of Records From Dataset

import pandas as pd

p= int(worker.shape[0])
worker.head(p/2)

#or

p = int(len(worker)/2)
worker.head(p)
