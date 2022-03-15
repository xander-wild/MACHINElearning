import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

data = pd.read_csv("review.csv")
print(data.head())
print(data.dropna())

#cleaning the dat a


import nltk
import re
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopword=set(stopwords.words('english'))

def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
data["Review"] = data["Review"].apply(clean)

#Sentiment Analysis of Flipkart Reviews
#The Rating column of the data contains the
# ratings given by every reviewer. So let’s 
#have a look at how most of the people rate 
#the products they buy from Flipkart:

ratings = data["Rating"].value_counts()
numbers = ratings.index
quantity= ratings.values

import plotly.express as px 
figure = px.pie(data,values=quantity,names=numbers,hole=0.5)

#So 60% of the reviewers have given 5 out of 5 
#ratings to the products they buy from Flipkart. 
#Now let’s have a look at the kind of reviews people 
#ave. For this, I will use a word cloud to visualize 
#the most used words in the reviews column:

text = " ".join(i for i in data.Review)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, 
                      background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title("Most words used in review ")
plt.axis("off")


#Now I will analyze the sentiments of Flipkart 
#reviews by adding three columns in this dataset
 #as Positive, Negative, and Neutral by calculating 
 #the sentiment scores of the reviews:

nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["Review"]]

data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["Review"]]

data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["Review"]]

data = data[["Review", "Positive", "Negative", "Neutral"]]

print(data.head())

#Now let’s see how most of the reviewers think 
#about the products and services of Flipkart:

x=sum(data["Positive"])

y=sum(data["Negative"])


z=sum(data["Neutral"])

def sentiment_score(a,b,c):
	if (a>b) and (a>c):
		print("positive emotions")
	elif (b>a) and (b>c):
		print("negatice emotions ")
	else:
		print("Neutral emotions ")

sentiment_score(x,y,z)
print("Positive: ", x)
print("Negative: ", y)
print("Neutral: ", z)

#So, most people give Neutral reviews, and a 
#small proportion of people give Negative reviews. 
# we can say that people are satisfied with Flipkart 
#products and services.

plt.show()
figure.show()
