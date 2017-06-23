import pandas as pd
from datetime import datetime
from datetime import date
import numpy as np
from matplotlib import pyplot as plt
import re

DJTdf = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllMysteryTweetsdataframe.pkl')

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

DJTdf['Tweettextscore'] = DJTdf.Tweettext.apply(sentscore)

def dateinfo(tweetcreationdate):
    a = datetime.strptime(tweetcreationdate[:19], '%a %b %d %X')
    b = a.replace(2017)
    return b

DJTdf['tweetdatetime'] = DJTdf.TweetCreationDate.apply(dateinfo)

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

DJTdf['tweetweekday'] = DJTdf.tweetdatetime.apply(weekday)

saturdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Saturday']
sundaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Sunday']
mondaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Monday']
tuesdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Tuesday']
# wednesdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Wednesday']
# thursdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Thursday']
# fridaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Friday']

dataframelist = [saturdaytweets, sundaytweets, mondaytweets, tuesdaytweets]

daylist = ['Saturday', 'Sunday', 'Monday', 'Tuesday']

meanlist = []
medianlist = []
stdlist = []

for item in dataframelist:
    a = item.Tweettextscore
    meanlist.append(round(a.mean(), 2))
    medianlist.append(round(a.median(), 2))
    stdlist.append(round(a.std(), 2))

daydataframe = pd.DataFrame([meanlist, medianlist, stdlist], index=['Mean', 'Median', 'std'], columns=daylist)

daydataframe.to_pickle('DJTTweetDataSummary.pkl')