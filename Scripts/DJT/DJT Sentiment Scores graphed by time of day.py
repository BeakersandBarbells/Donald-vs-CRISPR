import numpy as np
import pandas as pd
import simplejson
import re
import matplotlib.pyplot as plt
from datetime import datetime

openfile = open('DJTTweets2017-06-17+00 - Copy.json').read()

dict_list = [d.strip() for d in openfile.splitlines()]

tweetlist = []

for line in (dict_list):
    try:
        a = simplejson.loads(line)
        tweetlist.append(a)
    except:
        pass

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

def dateinfo(tweetcreationdate):
    a = datetime.strptime(tweetcreationdate[:19], '%a %b %d %X')
    b = a.replace(2017)
    return b

df['tweetdatetime'] = df.TweetCreationDate.apply(dateinfo)

print df.tweetdatetime

def sentscore(tweettext):
    a = tweettext.encode('ascii', 'ignore')
    b = str(a)
    c = re.sub("[^\w]", " ", b).split()
    #textlist = c.split()
    score = 0
    for word in c:
        if word in scores:
            score += scores[word]
    return score

df['Tweettextscore'] = df.Tweettext.apply(sentscore)

df['nozeroscores'] = (df.Tweettextscore).replace([0], [np.nan])

df.dropna()

#print df.Tweettextscore.describe()

barplot = plt.plot(df.tweetdatetime, df.nozeroscores)

#axes = plt.gca()
#axes.table(cellText=freqstats, rowLabels=freqstats.index, colLabels=None, loc='bottom')
#axes.set_xlim([-26,26])
#axes.set_ylim([0,14000])
#plt.ylabel('Frequency of Sentiment Score (log-scale)')
#plt.xlabel('Tweet Sentiment Score')
#plt.title('Donald Trump Tweet Sentiment By time of day' + '\n' + '6.17 - 6.19')

plt.show()