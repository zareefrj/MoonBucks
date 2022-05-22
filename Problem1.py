#READING THE TXT FILE
with open ("South Korea.txt","r",encoding="utf-8") as file:
    article=file.read()
    #print(var)
    file.close()
    pass

#DATA CLEANING

# 1.1: appending new stop words into existing lists in nltk
my_file = open("online stopwords.txt", "r")
new_sw = my_file.read()  
# replacing end splitting the text 
# when newline ('\n') is seen.
newSw_list = new_sw.split("\n")
my_file.close()

# 1.1: ADDING ONLINE STOP WORDS TO THE EXISTING NLTK LIBRARY
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk_stop_words = stopwords.words('english')
#print(nltk_stop_words) #lists of stop words in nltk package

final_stopword_list=nltk_stop_words + newSw_list

#1.2 : REMOVING & COUNTING STOPWORDS
#CREATE TEXTBLOB & SENTIMENT ANALYSIS
from textblob import TextBlob, Word
blob=TextBlob(article)
#print(blob)

#REMOVE STOPWORDS & LEMMATASIZE
#COUNTING STOPWORDS
stopword_freq=0
clean_data_1="" #store string with removed stopwords
for w in blob.words:
    word=Word(w)
    word.lemmatize()
    if word in final_stopword_list:
        stopword_freq+=1
        
    else:
        clean_data_1+=" "+word
    
print("No of Stop Words: ",stopword_freq)

#GET RID OF PUNCTUATIONS & MAKE IT ALL LOWERCASE
clean_data_2=clean_data_1.replace('[^\w\s]','')
#print(clean_data_2.split)
#SENTIMENT ANALYSIS
cleanblob=TextBlob(clean_data_2)
print("Overall Sentiment: ",round(cleanblob.sentiment.polarity,2)) # -1 negative, 0 neutral, +1 positive; 0 objective, 1 subjective
#print(cleanblob)
#COUNTING POSITIVE & NEGATIVE WORDS
pos_count=0; neg_count=0
for word in cleanblob.words:
    if TextBlob(word).sentiment.polarity>0:
        pos_count+=1
    #print the words?
    if TextBlob(word).sentiment.polarity<0:
        neg_count+=1

#POSITIVE & NEGATIVE %
pos_percent=round((pos_count*100)/(pos_count+neg_count),2)
neg_percent=round(100-pos_percent,2)
print("No of Positive Words: ",pos_count,"(",pos_percent,"%)")
print("No of Negative Words: ",neg_count,"(",neg_percent,"%)")