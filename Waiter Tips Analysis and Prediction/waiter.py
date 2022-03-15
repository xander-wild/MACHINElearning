import pandas as pd 
import numpy as np 
import plotly.express as px 
import plotly.graph_objects as go 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("tips.csv")
#print(data.head())

#Let’s have a look at the tips given to the waiters according to:

#the total bill paid
#number of people at a table
#and the day of the week:

#day

figure = px.scatter(data_frame = data, x="total_bill",y="tip", size="size", color= "day", trendline="ols")
figure.show()

#gender 

figure = px.scatter(data_frame = data, x="total_bill",y="tip", size="size", color= "sex", trendline="ols")
figure.show()

#time 

figure = px.scatter(data_frame = data, x="total_bill",y="tip", size="size", color= "time", trendline="ols")
figure.show()

#Now let’s see the tips given to the waiters
#according to the days to find out which day the most tips are given to the waiters:


figure = px.pie(data, 

             values='tip', 

             names='day',hole = 0.5)

figure.show()

figure = px.pie(data, 

             values='tip', 

             names='smoker',hole = 0.5)

figure.show()

figure = px.pie(data, 

             values='tip', 

             names='time',hole = 0.5)

figure.show()

#waiter tip prediciton model 

data["sex"]=data["sex"].map({"Female":0,"Male":1})
data["smoker"]=data["smoker"].map({"No":0,"Yes":1})
data["day"]=data["day"].map({"Thur":0,"Fri":1,"Sat":2,"Sun":3})
data["time"]=data["time"].map({"Lunch":0,"Dinner":1})

print(data.head())

#now split the data into training and test sets ;

x= np.array(data[["total_bill","sex","smoker","day","time","size"]])

y= np.array(data["tip"])

xtrain , xtest , ytrain , ytest = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(xtrain,ytrain)

#Now let’s test the performance of this model by giving inputs to this model according to the features that we have used to train this model:


# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]


total_bill = int(input("total_bill : "))
sex= int(input("for female:0,for male:1 : "))
smoker=int(input("0/1 for no or yes for smoker: "))
day=int(input("Thur:0,Fri:1,Sat:2,Sun:3 : "))
time = int (input("time: lunch :0,dinner:1 :"))
size = int(input("size of the table "))




features = np.array([[total_bill,sex,smoker,day,time,size]])

print("tip will be aprox.",model.predict(features))






