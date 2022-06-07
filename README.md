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

![image](https://user-images.githubusercontent.com/76507749/170492209-fba53396-0ac1-4548-8582-18bb510f5feb.png)
### Step 4: Ploting
A bar chart is created to visualize the sentiment score of each country. The bar chart is chosen to represent this because the data is categorical & not continuous (i.e. the x-axis are the countries. In contrast, other charts like histograms are for continuous & numerical data in which the data can aggreated into bins (range groups), this creates a continuous gapless chart. In addition, a bar chart is perfect for showing the contrast between the countries, which aids in decision making.
Only the sentiment score of the countries are plotted as we believe that that metric is enough for proceeding analysis as the ratio between the positive & negative sentiments are into account into the overall sentiment score.

![image](https://user-images.githubusercontent.com/76507749/170492461-15497842-b465-4252-90e2-cf08fb7ac1fc.png)
## Sentiment Analysis Time Complexity
**O(n); n is the no of words in the text file.** The algorithm checks for every word in the text file against TextBlob (nltk package)'s library, then sums up the sentiment scores of all the words. To make it more efficient & faster, stop words & punctuations are removed as they do not contribute to the overall sentiment score.
## PROBLEM 2
### Step 1: Finding distribution Centre
Since Google API required us to create billing account, we resolve to use free API for the time being.\
API : https://rapidapi.com/trueway/api/trueway-matrix

### Step 2: Finding the optimal route
Christofides' Algorithm is a 1.5-approximation algorithm.\
Time Complexity: $O(|V|^4)$ : which is significantly better than any of the exact solution approaches.\
Source: https://cse442-17f.github.io/Traveling-Salesman-Algorithms/

Using Geocoding library

I found this YouTube video on how to use the Geocoding Library

[![Geocoding Library](https://img.youtube.com/vi/d1QGLwie9YU/0.jpg)](http://www.youtube.com/watch?v=d1QGLwie9YU)

## PROBLEM 3
``The probability of a country that has a good local economic and social situation with the
lowest optimal delivery.``

I'm not sure about it but I think for this problem, we can calcukate the probability by using below formula:

![algo group project probability](https://user-images.githubusercontent.com/59971431/172339009-30b69c98-f180-4c8e-a42a-dc245a4ab22e.png)
