import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({'A': 1.,
                      'B': pd.Timestamp('20130102'),
                       'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                       'D': np.array([3] * 4, dtype='int32'),
                       'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

df2 = df.copy()
df2[df2 > 0] = -df2
d=pd.read_csv('TANDS.csv')
#df1 = df.reindex(index=dates[0:4], columns=list(df.columns))
df.to_csv('foo.csv')
print(d)