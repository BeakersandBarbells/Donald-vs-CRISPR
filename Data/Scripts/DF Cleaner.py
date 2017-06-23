import pandas as pd
import simplejson
import re
from datetime import date
import numpy as np
from datetime import datetime

#this script opens two different JSON docs from my tweet streamers, compiles them into a big list, converts to a dataframe, then dumps them into a .pkl file. Neat!

rawdata1 = open('C:\Users\m144851\Desktop\Github '
                'Projects\Donald-vs-CRISPR\Data\Raw\MysteryTweets2017-06-20+00.json').read()

#rawdata2 = open('C:\Users\m144851\Desktop\Github '
#                'Projects\Donald-vs-CRISPR\Data\Raw\DJTTweets2017-06-21+00.json').read()

cleandata1 = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllMysteryTweetsdataframe.pkl')

dict_list1 = [d.strip() for d in rawdata1.splitlines()]
#dict_list2 = [d.strip() for d in rawdata2.splitlines()]

tweetlist1 = []
#tweetlist2 = []

for line in (dict_list1):
    try:
        a = simplejson.loads(line)
        tweetlist1.append(a)
    except:
        pass

# for line in (dict_list2):
#     try:
#         a = simplejson.loads(line)
#         tweetlist2.append(a)
#     except:
#         pass

df = pd.DataFrame(tweetlist1)
#df1 = pd.DataFrame(tweetlist2)

newdf = pd.concat([df, cleandata1], ignore_index=True)

doc = open(
    'C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\AFINN-en-165.txt',
    'r')

scores = {}
for line in doc:
    term, score = line.split("\t")
    scores[term] = int(score)

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

newdf['Tweettextscore'] = newdf.Tweettext.apply(sentscore)

def dateinfo(tweetcreationdate):
    a = datetime.strptime(tweetcreationdate[:19], '%a %b %d %X')
    b = a.replace(2017)
    return b

newdf['tweetdatetime'] = newdf.TweetCreationDate.apply(dateinfo)

def weekday(datetimeday):
    if date.weekday(datetimeday) == 0:
        return 'Monday'
    elif date.weekday(datetimeday) == 1:
        return 'Tuesday'
    elif date.weekday(datetimeday) == 2:
        return 'Wednesday'
    elif date.weekday(datetimeday) == 3:
        return 'Thursday'
    elif date.weekday(datetimeday) == 4:
        return 'Friday'
    elif date.weekday(datetimeday) == 5:
        return 'Saturday'
    elif date.weekday(datetimeday) == 6:
        return 'Sunday'

newdf['tweetweekday'] = newdf.tweetdatetime.apply(weekday)

newdf.to_pickle('AllMysteryTweetsdataframe-1.pkl')