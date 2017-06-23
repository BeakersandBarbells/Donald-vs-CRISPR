import pandas as pd
from datetime import datetime
from datetime import date

basedf = pd.read_pickle('AllCRISPRTweetsdataframe.pkl')

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

basedf.tweetweekday
saturdaytweets = basedf.loc[basedf['tweetweekday'] == 'Saturday']
sundaytweets = basedf.loc[basedf['tweetweekday'] == 'Sunday']
mondaytweets = basedf.loc[basedf['tweetweekday'] == 'Monday']
tuesdaytweets = basedf.loc[basedf['tweetweekday'] == 'Tuesday']
wednesdaytweets = basedf.loc[basedf['tweetweekday'] == 'Wednesday']
thursdaytweets = basedf.loc[basedf['tweetweekday'] == 'Thursday']
fridaytweets = basedf.loc[basedf['tweetweekday'] == 'Friday']