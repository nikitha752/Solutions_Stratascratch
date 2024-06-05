import pandas as pd

crunchbase_acquisitions['quarter'] = crunchbase_acquisitions['acquired_quarter'].dt.year.astype(str) + '-Q' + crunchbase_acquisitions['acquired_quarter'].dt.quarter.astype(str)
crunchbase_acquisitions.groupby('quarter').size().to_frame('size').reset_index().sort_values('size', ascending=False)
