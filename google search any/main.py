import pandas as pd 
import matplotlib.pyplot as plt 
from pytrends.request import TrendReq

trends = TrendReq(hl='en-US',tz=360)

 #I will be analyzing the Google search 
 #trends on the queries based on “Machine Learning”,
 # so let’s create a DataFrame of the 
# top 10 countries which search for
# “Machine Learning” on Google:
#for user input 

#search = input("What you want to search")

search=["Macchine Learning"]
#for default
trends.build_payload(kw_list=search)

#taking data by region 

data = trends.intrest_by_region(resolution='COUNTRY')

data= data.sort_values(by=search,ascending = False)

#showing top 10

data=data.head(10)

print(data)
data.reset_index().plot(x="geoName", y="Machine Learning", 
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data['Machine Learning'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Machine Learning', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()

