import numpy as np
import pandas as pd
import simplejson
import re
import matplotlib.pyplot as plt

df = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllDJTTweetsdataframe.pkl')

doc = open('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\AFINN-en-165.txt', 'r')

scores = {}
for line in doc:
    term, score = line.split("\t")
    scores[term] = int(score)

#print df.columns.values

#df columns are
# ['Coordinates' 'Favorites' 'Hashtags' 'Retweets' 'TweetCreationDate' 'TweetID' 'Tweettext' 'UserBirth' 'UserID'
# 'UserTweetCount' 'Userfollowers' 'Username' 'Usertimezone' 'Verified']


def sentscore(tweettext):
    a = tweettext.encode('ascii', 'ignore')
    b = str(a)
    c = re.sub("[^\w]", " ", b).split()
    score = 0
    counter = 0
    for word in c:
        if word in scores:
            score += scores[word]
            counter += 1
    if counter >= 1:
        return score
    else:
        return np.nan

df['Tweettextscore'] = df.Tweettext.apply(sentscore)

averagesentscore = round(df.Tweettextscore.mean(), 2)

scorefreqs = df.Tweettextscore.value_counts(sort=False)

freqstats = scorefreqs.describe()

freqstats = freqstats.round(decimals=2)

barplot = plt.bar(scorefreqs.index, scorefreqs.values)

axes = plt.gca()
#axes.table(cellText=freqstats, rowLabels=freqstats.index, colLabels=None, loc='bottom')
axes.set_xlim([-26,26])
#axes.set_ylim([0,14000])
plt.ylabel('Frequency of Sentiment Score')
plt.xlabel('Tweet Sentiment Score')
plt.title('Donald Trump Tweet Sentiment Score Frequency' + '\n' + '6.17 - 6.19')

plt.show()