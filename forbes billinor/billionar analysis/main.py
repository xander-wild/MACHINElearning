# dataset used Billionaire.csv
#Names
#Net Worth 
#Country 
#Source 
#Rank
#Age
#Industry

import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = pd.read_csv("Billionaire.csv")
#print(data.head())

#finding null data 

print(data.isnull().sum())

# we can see age have 79 missing value so we will drop it 

data = data.dropna()

data["NetWorth"] = data["NetWorth"].str.strip("$")
data["NetWorth"] = data["NetWorth"].str.strip("B")
data["NetWorth"] = data["NetWorth"].astype(float)

print(data)

# lets look at top 10 billinoaiers ac to net worth 

df= data.sort_values(by = ["NetWorth"], ascending = False).head(10)

plt.figure(figsize = (20,10))
sns.histplot(x ="Name",hue="NetWorth",data= df)
#plt.show()

# now lets have a look at the top 5 domains with the most no of billionaires:

a= data["Source"].value_counts().head()
index = a.index
sources = a.values 
custom_colors = ["skyblue","yellowgreen","tomato","blue","red"]
plt.figure(figsize=(10,10))
plt.pie(sources, labels = index , colors = custom_colors)
central_circle = plt.Circle((0,0),0.5,color="white")

fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Domains to Become a Billionaire", fontsize=20)


# now lets have a look at the top 5 industry with the most no of billionaires:


a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(10,10))
plt.pie(industries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Industries with Most Number of Billionaires", fontsize=20)


# now lets have a look at the top 5 country with the most no of billionaires:

a = data["Country"].value_counts().head()
index = a.index
Countries = a.values
custom_colors = ["skyblue", "yellowgreen", 'tomato', "blue", "red"]
plt.figure(figsize=(10,10))
plt.pie(Countries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Countries with Most Number of Billionaires", fontsize=20)


plt.show()

# this data shows the data of the billioner and in which secotor they are making the most amount of monty 
# in whihc country and in whihc domain 
# domain ---- real estate 
# industry ---- finacnce and investing 
# country ------ united state 
