import pandas as pd
from datetime import datetime
from datetime import date
import numpy as np
from matplotlib import pyplot as plt
import re

basedf = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllDJTTweetsdataframe.pkl')

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

basedf['Tweettextscore'] = basedf.Tweettext.apply(sentscore)

def dateinfo(tweetcreationdate):
    a = datetime.strptime(tweetcreationdate[:19], '%a %b %d %X')
    b = a.replace(2017)
    return b

basedf['tweetdatetime'] = basedf.TweetCreationDate.apply(dateinfo)

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

basedf['tweetweekday'] = basedf.tweetdatetime.apply(weekday)

saturdaytweets = basedf.loc[basedf['tweetweekday'] == 'Saturday']
sundaytweets = basedf.loc[basedf['tweetweekday'] == 'Sunday']
mondaytweets = basedf.loc[basedf['tweetweekday'] == 'Monday']
tuesdaytweets = basedf.loc[basedf['tweetweekday'] == 'Tuesday']
wednesdaytweets = basedf.loc[basedf['tweetweekday'] == 'Wednesday']
thursdaytweets = basedf.loc[basedf['tweetweekday'] == 'Thursday']
fridaytweets = basedf.loc[basedf['tweetweekday'] == 'Friday']

Saturday = saturdaytweets.Tweettextscore.value_counts(sort=False)
Sunday = sundaytweets.Tweettextscore.value_counts(sort=False)
Monday = mondaytweets.Tweettextscore.value_counts(sort=False)
Tuesday = tuesdaytweets.Tweettextscore.value_counts(sort=False)
#wedscorefreqs = wednesdaytweets.Tweettextscore.value_counts(sort=False)
#thurscorefreqs = thursdaytweets.Tweettextscore.value_counts(sort=False)
#friscorefreqs = fridaytweets.Tweettextscore.value_counts(sort=False)

Saturday.name = "Saturday"
Sunday.name = "Sunday"
Monday.name = "Monday"
Tuesday.name = "Tuesday"

freqlist = [Saturday, Sunday, Monday, Tuesday]

def figuremaker(dataframelist):
    figureno = 0
    for item in dataframelist:
        plt.figure(figureno)
        plt.bar(item.index, item.values)
        axes = plt.gca()
        axes.set_xlim([-15, 15])
        plt.ylabel('Frequency of Sentiment Score')
        plt.xlabel('Tweet Sentiment Score')
        plt.title('Donald Trump Tweet Sentiment Score Frequency' + '\n' + item.name)
        plt.savefig('Donald Trump Tweet Sentiment - ' + item.name + '.png')
        figureno += 1
    return plt.show

figuremaker(freqlist)

plt.show()

# wedsfreqstats = wedscorefreqs.describe()
#
# wedsfreqstats = wedsfreqstats.round(decimals=2)
#
# barplot = plt.bar(wedscorefreqs.index, wedscorefreqs.values)

# axes = plt.gca()
# axes.set_xlim([-26,26])
# plt.ylabel('Frequency of Sentiment Score')
# plt.xlabel('Tweet Sentiment Score')
# plt.title('CRISPR Tweet Sentiment Score Frequency' + '\n' + 'Wednesday')

# plt.savefig('CRISPR Tweet Sentiment - Wednesday 6.20.17.png')
#
# plt.show()