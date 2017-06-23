import pandas as pd
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllCRISPRTweetsdataframe.pkl')

df = df.drop(df[np.isnan(df.Tweettextscore) == True].index)

saturdaytweets = df.loc[df['tweetweekday'] == 'Saturday']
sundaytweets = df.loc[df['tweetweekday'] == 'Sunday']
mondaytweets = df.loc[df['tweetweekday'] == 'Monday']
tuesdaytweets = df.loc[df['tweetweekday'] == 'Tuesday']
wednesdaytweets = df.loc[df['tweetweekday'] == 'Wednesday']

satcleanscores = saturdaytweets.Tweettextscore.dropna()
suncleanscores = sundaytweets.Tweettextscore.dropna()
moncleanscores = mondaytweets.Tweettextscore.dropna()
tuescleanscores = tuesdaytweets.Tweettextscore.dropna()
wedscleanscores = wednesdaytweets.Tweettextscore.dropna()

#df.boxplot('Tweettextscore', by='tweetweekday')
grps = pd.unique(df.tweetweekday.values)
d_df = {grp:df['Tweettextscore'][df.tweetweekday == grp] for grp in grps}
k = len(pd.unique(df.tweetweekday))
N = len(df.Tweettextscore.values)
n0 = df.groupby('tweetweekday').size()[0]
n1 = df.groupby('tweetweekday').size()[1]
n2 = df.groupby('tweetweekday').size()[2]
n3 = df.groupby('tweetweekday').size()[3]
n4 = df.groupby('tweetweekday').size()[4]

f, p = stats.f_oneway(d_df['Saturday'], d_df['Sunday'], d_df['Monday'], d_df['Tuesday'], d_df['Wednesday'])

plt.boxplot([satcleanscores.values, suncleanscores, moncleanscores, tuescleanscores, wedscleanscores], notch=True, labels=['Saturday' + '\n' + 'N: '+ str(n0), 'Sunday', 'Monday', 'Tuesday', 'Wednesday'])
plt.axhline(y=0, lw=0.5, ls='dashed')
plt.xlabel('Day of the Week')
plt.ylabel('Sentiment Score')
plt.title('CRISPR Sentiment Scores')
plt.savefig('CRISPR Sentiment Score Boxplots.png')

print 'F Value: ' + str(round(f, 2))
print 'P Value: ' + str(p)
print 'Unique groups: ' + str(k)
print 'Number of Observations: ' + str(N)
print 'N-Saturday: ' + str(n0)
print 'N-Sunday: ' + str(n1)
print 'N-Monday: ' + str(n2)
print 'N-Tuesday: ' + str(n3)
print 'N-Wednesday: ' + str(n4)

plt.show()