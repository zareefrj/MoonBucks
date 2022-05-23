# MoonBucks
Algorithm Design Semester 2 2021/22 Group 3 Project. ***THESE ARE MY APPROACHES SO FAR, IF YOU HAVE ANY BETTER IDEAS/SUGGESTIONS, FEEL FREE TO DISCUSS FURTHER***
## PROBLEM 1
### Step 1: Extracting the words from the articles
#### Approach 1 (Unsuccessful)
use webscrapping to scrap the data from the articles online, but the each website layout is different, meaning we need to tweak how it scrapes for every website.
#### Approach 2 (Unsuccessful) 
use the pdf we compiled by reading the files directly & extracting the texts. But, the issue is the pdf needs to be fully in text, any images will interfere the reading process.
#### Approach 3 (Current)
might as well [Textify](https://www.textise.net/) the websites, & then manually copy pasting only the necessary paragraphs into a notepad (txt file , _refer the South Korea file_)
### Step 2: Cleaning the data
removed the punctuations, stopwords (counting them as well) & lowering all letters to lowercase. For stopwords, I combined nltk's stopwords library with the online stopwords from what Dr shared.
`import nltk`
`from nltk.corpus import stopwords`
`nltk.download('stopwords')`
`nltk.download('omw-1.4')`
`nltk_stop_words = stopwords.words('english')`
`final_stopword_list=nltk_stop_words + newSw_list`
### Step 3: Sentiment Analysis
Used [TextBlob](https://textblob.readthedocs.io/en/dev/) built in library to do sentiment analysis. How TextBlob does this: https://planspace.org/20150607-textblob_sentiment/
TextBlob inner workings: https://youtu.be/Y8iNez1tCx8 TextBlob Tutorial: https://youtu.be/pkdmcsyYvb4
### Step 4: Ploting
So far I am experimenting on the bar charts...you can use the TextBlob Test file to try things out for yourself.
