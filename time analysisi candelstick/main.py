import pandas as pd 
import yfinance as yf 
import datetime
from datetime import date, timedelta

#downloding and shifting data  

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=720)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2 
data = yf.download('AAPL',start=start_date,end=end_date,progress=False)
print(data.head())
#apple stock data 

import plotly.express as px 
# make the x and y axis with px 

figure = px.line(data,x=data.index,y="Close",title="Time series analysisi")
#figure.show()

#this gives us line graph but we also need candelsticks

import plotly.graph_objects as go

figure = go.Figure(data=[go.Candlestick(x=data.index,open = data["Open"], 
                                        high = data["High"],
                                        low = data["Low"], 
                                        close = data["Close"])])
figure.update_layout(title = "Time Series Analysis (Candlestick Chart)", 
                     xaxis_rangeslider_visible = False)
#figure.show()

figure.update_xaxes(
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
            dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
            dict(step = "all")
        ])
    )
)
figure.show()