import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob 
from wordcloud import WordCloud, STOPWORDS
import emoji
from collections import Counter
import plotly.graph_objs as go
import plotly.offline as pyo

# Importing the Database
df = pd.read_csv(
    r"C:\Users\Gulbaaz\Downloads\Analytics\Python_youtube_Analysis-master\video_id_info.csv",
    on_bad_lines='skip'
)
print(df)

# Find out the missing values
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())

## Perform Sentinent Analysis
polarity = []
for comment in df['comment_text']:
    try:
        polarity.append(TextBlob(comment).sentiment.polarity)
    except:
        polarity.append(0)
df['polarity'] = polarity
print(df.head(5))

## Wordcloud Analysis of Data
filter1 = df['polarity'] == 1
comment_positive = df[filter1]
total_comments_positive = ' '.join(comment_positive['comment_text'].astype(str))
wordcloud = WordCloud(stopwords=set(STOPWORDS), width=800, height=400, background_color = 'white').generate(total_comments_positive)
plt.figure(figsize = (12,6))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()
# conclusion : Positive Users are emphasizing more on best , awesome , perfect , amazing , look , happy  etc.
filter2 = df['polarity'] == -1
comment_negative = df[filter2]
total_comments_negative = ' '.join(comment_negative['comment_text'].astype(str))
wordcloud = WordCloud(stopwords=set(STOPWORDS), width=800, height=400, background_color = 'white').generate(total_comments_negative)
plt.figure(figsize = (12,6))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()
# conclusion : Negative Users are emphasizing more on Terrible , worst ,horrible ,boring , disgusting etc.

## Perform Emoji's Analysis
all_emojis_list = []
for comment in df['comment_text']:
    for ch in comment:
        if ch in emoji.EMOJI_DATA:
            all_emojis_list.append(ch)
print("Sample emojis:", all_emojis_list[:10])
freq = Counter(all_emojis_list).most_common(10)
emojis = [e[0] for e in freq]
counts = [e[1] for e in freq]
fig = go.Figure(data=[go.Bar(x=emojis, y=counts)])
fig.update_layout(title = "Top 10 Emojis in Comments", xaxis_title = "Emoji", yaxis_title = "Frequency", template = "plotly_dark")
fig.show()
#Conclusions : Majority of the customers are happy as most of them are using emojis like: funny , love , heart , outstanding.
