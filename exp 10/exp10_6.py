import pandas as pd
import numpy as np

data = {
    'A': [1,2,np.nan,4],
    'B': [5,np.nan,np.nan,8],
    'C': [10,11,12,np.nan]
}

df = pd.DataFrame(data)

filled = df.fillna(df.mean())
dropped = df.dropna()

print(filled)
print(dropped)