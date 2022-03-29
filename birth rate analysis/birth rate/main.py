import pandas as pd 
data = pd.read_csv("births.csv")
print(data.head())

data["decade"]=10*(data["year"]//10)
data.pivot_table('births',index= 'decade',columns='gender',aggfunc='sum')
print(data.head())


import matplotlib.pyplot as plt 

import seaborn as sns 

sns.set()

birth_decade = data.pivot_table('births', index='decade', columns='gender', aggfunc='sum') 

birth_decade.plot() 

plt.ylabel("Total births per year") 



#further data xploration 
#removing outliers caused by mistyped dates or missing values. 

import numpy as np 

qt = np.percentile(data['births'],[25, 50, 75])
mu=qt[1]
sig =0.74*(qt[2]-qt[0])


births = data.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')

births['dayofweek'] = births.index.dayofweek

#Using this we can plot births by weekday for several decades:

births.pivot_table('births', index='dayofweek',
                    columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');

births_month = births.pivot_table('births', [births.index.month, births.index.day])
print(births_month.head())


births_month.index = [pd.datetime(2012, month, day)
                      for (month, day) in births_month.index]
print(births_month.head())

fig, ax = plt.subplots(figsize=(12, 4))
births_month.plot(ax=ax)

plt.show()