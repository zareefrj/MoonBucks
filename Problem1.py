#ADDING ONLINE STOP WORDS TO THE EXISTING NLTK LIBRARY
#THIS PART IS CONSTANT FOR EVERY SENTIMENT ANALYSIS, THEREFORE IT IS IN THE MAIN METHOD
my_file = open("online stopwords.txt", "r")
new_sw = my_file.read()  
# replacing end splitting the text 
# when newline ('\n') is seen.
newSw_list = new_sw.split("\n")
my_file.close() 
import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk_stop_words = stopwords.words('english')
#print(nltk_stop_words) #lists of stop words in nltk package
final_stopword_list=nltk_stop_words + newSw_list

#Sentiment Analysis
def SentimentAnalysis(country, file_name):
    #READING THE TXT FILE
    with open (file_name,"r",encoding="utf-8") as file:
        article=file.read().lower()
        #print(var)
        file.close()
        pass

    #DATA CLEANING

    #CREATE TEXTBLOB & SENTIMENT ANALYSIS
    from textblob import TextBlob
    blob=TextBlob(article)
    #print(blob)

    #REMOVE & COUNTING STOPWORDS
    stopword_freq=0
    clean_data_1="" #store string with removed stopwords
    for word in blob.words:
        
        if word in final_stopword_list:
            stopword_freq+=1
            
        else:
            clean_data_1+=" "+word
        
    #removing punctuations
    punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for x in punctuation:
        clean_data_1=clean_data_1.replace(x," ")

    #SENTIMENT ANALYSIS
    cleanblob=TextBlob(clean_data_1)
    print("\n",country)
    #print("Overall Sentiment: ",round(cleanblob.sentiment.polarity,2)) # -1 negative, 0 neutral, +1 positive; 0 objective, 1 subjective
    #print(cleanblob)
    #COUNTING POSITIVE & NEGATIVE WORDS
    print("No of Stop Words: ",stopword_freq)
    pos_count=0; neg_count=0
    pos_words_list=[]
    neg_words_list=[]
    for word in cleanblob.words:
        if TextBlob(word).sentiment.polarity>0 and TextBlob(word) not in pos_words_list:
            pos_count+=1
            pos_words_list.append(word) #for storing the words
        
        if TextBlob(word).sentiment.polarity<0 and TextBlob(word) not in neg_words_list:
            neg_count+=1
            neg_words_list.append(word) #list to avoid counting the same word again

    #POSITIVE & NEGATIVE %
    pos_percent=round((pos_count*100)/(pos_count+neg_count),2)
    neg_percent=round(100-pos_percent,2)
    print("No of Positive Words: ",pos_count,"(",pos_percent,"%)")
    #print(pos_words_list)
    print("No of Negative Words: ",neg_count,"(",neg_percent,"%)")
    #print(neg_words_list)

    return round(cleanblob.sentiment.polarity,2)

#plot method
def plotChart(country):
    import plotly.graph_objects as go
    fig = go.Figure(
            data=[go.Bar(x=country, y=[SentimentAnalysis(country[0], country[0]+".txt"),
            SentimentAnalysis(country[1], country[1]+".txt"),SentimentAnalysis(country[2], country[2]+".txt"),
            SentimentAnalysis(country[3], country[3]+".txt"),SentimentAnalysis(country[4], country[4]+".txt")])],
            layout=go.Layout(
                title=go.layout.Title(text="The Sentiment of Countries")
            )
        )

    fig.show()

### DRIVER CODE ####
countries=["Great Britain","Canada","Japan","South Korea","Germany"]
#for country in countries:
plotChart(countries)