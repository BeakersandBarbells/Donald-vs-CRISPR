import pandas as pd
from matplotlib import pyplot as plt

DJTdf = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllCRISPRTweetsdataframe.pkl')

saturdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Saturday']
sundaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Sunday']
mondaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Monday']
tuesdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Tuesday']
wednesdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Wednesday']
# thursdaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Thursday']
# fridaytweets = DJTdf.loc[DJTdf['tweetweekday'] == 'Friday']

listthing = [saturdaytweets, sundaytweets, mondaytweets, tuesdaytweets]

satcleanscores = saturdaytweets.Tweettextscore.dropna()
suncleanscores = sundaytweets.Tweettextscore.dropna()
moncleanscores = mondaytweets.Tweettextscore.dropna()
tuescleanscores = tuesdaytweets.Tweettextscore.dropna()
wedscleanscores = wednesdaytweets.Tweettextscore.dropna()

plt.boxplot([satcleanscores.values, suncleanscores, moncleanscores, tuescleanscores, wedscleanscores], notch=True, labels=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'])
plt.axhline(y=0, lw=0.5, ls='dashed')
plt.xlabel('Day of the Week')
plt.ylabel('Sentiment Score')
plt.title('CRISPR Sentiment Scores')
plt.savefig('CRISPR Sentiment Score Boxplots.png')
plt.show()
