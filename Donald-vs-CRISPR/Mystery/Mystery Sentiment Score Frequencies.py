import numpy as np
import pandas as pd
import simplejson
import re
import matplotlib.pyplot as plt

openfile = open('MysteryTweets2017-06-17+00.json').read()

dict_list = [d.strip() for d in openfile.splitlines()]

tweetlist = []

for line in (dict_list):
    a = simplejson.loads(line)
    tweetlist.append(a)

df = pd.DataFrame(tweetlist)

doc = open('C:\Users\m144851\Dropbox\Personal\Education\Independent Learning\Data Science\Projects\CRISPR Sentiment\AFINN-en-165.txt', 'r')

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
    #textlist = c.split()
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
plt.title('Mystery Tweet Sentiment Score Frequency' + '\n' + '6.17 - 6.19')

plt.show()