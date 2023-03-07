import pandas as pd
#it is a library used to data ananlaysis and associate maniculation of tabular data
df=pd.read_csv('C://hcl1/capturedpacket.csv')
print(df.columns)
print(df.groupby('Protocol').sum())