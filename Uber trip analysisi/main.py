import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv("uber.csv")
data["Date/Time" ] = data["Date/Time"].map(pd.to_datetime)

#print(data.head(10))

data["Day"]= data["Date/Time"].apply(lambda x:x.day)
data["Weekday"] = data["Date/Time"].apply(lambda x: x.weekday())
data["Hour"] = data["Date/Time"].apply(lambda x:x.hour)

#print(data.head(10))

sns.set(rc={'figure.figsize':(12, 10)})
sns.distplot(data["Day"])

sns.distplot(data["Hour"])

sns.distplot(data["Weekday"])

df= data.groupby(["Weekday","Hour"]).apply(lambda x:len(x))

df =df.unstack()

sns.heatmap(df, annot = False)

data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',

figsize=(12, 8), cmap=plt.get_cmap('jet'))

plt.title("Uber Trips Analysis")
plt.legend()
plt.show()

#So this is how we can analyze the Uber trips for New York City. Some of the conclusions that I got from this analysis are:

#Monday is the most profitable day for Uber
#On Saturdays less number of people use Uber
#6 pm is the busiest day for Uber
#On average a rise in Uber trips start around 5 am.
#Most of the Uber trips originate near the Manhattan region in New York.
