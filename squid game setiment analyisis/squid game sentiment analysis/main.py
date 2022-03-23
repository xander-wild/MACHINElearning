#data set used datasquid.py
import pandas as pd 

import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


#cleaning the data 
print("avaliable data set : \n datasquid.csv ")
file_name = input("enter the name of the file u wnat to do sentiment alayisis on :")
file_name = "datasquid.csv"
data = pd.read_csv(file_name)
#print(data.head())

data = data.drop(columns= "user_location",axis = 1)



# we can see that user_description is nan so we drop it

data= data.drop(columns = "user_description",axis = 1)
data= data.dropna()

print(data.head())

#print(data.isnull().sum())

# now we have no nan data 

#The “text” column in the dataset contains the opinions of the users of Twitter about the squid game

import nltk
import re
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string
stopword=set(stopwords.words('english'))


#cleaning the text  we can use this in future also 



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

data["text"]= data["text"].apply(clean)

print(data["text"].head())

#Now let’s take a look at the most used words in the Squid Game opinions
#using a word cloud. A word cloud is a data visualization tool that displays 
#the most used words in a larger size.

text = " ".join(i for i in data.text)

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords =  stopwords,background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

print("Now let’s move to the task of \n  sentiment analysis. Here I will \n add three more columns in this dataset\n as Positive, Negative, and Neutral by \n calculating the sentiment scores of the text column")

nltk.download('vader_lexicon')
sentiments = SentimentIntensityAnalyzer()
data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["text"]]
data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["text"]]
data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["text"]]
data = data[["text", "Positive", "Negative", "Neutral"]]
print(data.head())

print("now lets calculate how most people think about ")

x = sum(data["Positive"])
y = sum(data["Negative"])
z = sum(data["Neutral"])

def sentiment_score(a, b, c):
    if (a>b) and (a>c):
        print("Positive 😊 ")
    elif (b>a) and (b>c):
        print("Negative 😠 ")
    else:
        print("Neutral 🙂 ")
sentiment_score(x, y, z)
print(" this data is taken from twiiter comments")

print("So most of the opinions of the users are Neutral, now let’s have a look at the total of each sentiment score before making any conclusion:")

print("Positive: ",x)
print("Negative: ", y)
print("Neutral: ", z)