#YOU CAN USE THIS FILE TO EXPERIMENT ON TEXTBLOB or other stuff :)
#READING THE TXT FILE
"""with open ("testtext.txt","r",encoding="utf-8") as file:
    var=file.read().lower() #Lowercase everything
    #print(var)
    file.close()
    pass

from textblob import Word
v=Word("friends")
print(v.lemmatize()) #only changes plural to singular

#removing punctuations
punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for x in punctuation:
    var=var.replace(x,"")
print(var)
"""
#PLOTLY
#$ pip install plotly==5.8.0
#try scatter or line
import plotly.graph_objects as go
fig = go.Figure(
        data=[go.Bar(x=["kl"], y=[1])],
        layout=go.Layout(
            title=go.layout.Title(text="The Sentiment of Countries")
        )
    )

fig.show()
#for i in range(5): it creates individual graphs