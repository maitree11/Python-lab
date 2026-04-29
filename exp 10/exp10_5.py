import pandas as pd
import numpy as np

exam_data = {
'name': ['Maitree','Ritik', 'Divyanka','Kohinoor','Janvi','Sneha', 'Rudra','Simmba','Laura','Kevin'],
'score': [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
'attempts': [1,3,2,3,2,3,1,1,2,1],
'qualify': ['yes','no','yes','no','no','yes','yes','no','no','yes']
}

labels = list('abcdefghij')

df = pd.DataFrame(exam_data, index=labels)

print(df.head(3))