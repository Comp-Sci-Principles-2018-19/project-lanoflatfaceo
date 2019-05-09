import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('TANDS.csv')
#df1 = df.reindex(index=dates[0:4], columns=list(df.columns))
ric=df["R"]
deaths=df["D"]
pop=df["pop"]
deathsper=deaths/pop
print(deathsper)




plt.scatter(deathsper,ric)
plt.show()