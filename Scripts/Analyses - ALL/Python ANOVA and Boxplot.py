import pandas as pd
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_pickle('C:\Users\m144851\Desktop\Github Projects\Donald-vs-CRISPR\Data\Clean\AllMysteryTweetsdataframe.pkl')

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

grps = pd.unique(df.tweetweekday.values)
d_df = {grp:df['Tweettextscore'][df.tweetweekday == grp] for grp in grps}
k = len(pd.unique(df.tweetweekday))
N = len(df.Tweettextscore.values)
Nvalues = df.groupby('tweetweekday').size().values

n0 = df.groupby('tweetweekday').size()[0]
n1 = df.groupby('tweetweekday').size()[1]
n2 = df.groupby('tweetweekday').size()[2]
n3 = df.groupby('tweetweekday').size()[3]
n4 = df.groupby('tweetweekday').size()[4]

NValueslist = [n0, n1, n2, n3, n4]

f, p = stats.f_oneway(d_df['Saturday'], d_df['Sunday'], d_df['Monday'], d_df['Tuesday'], d_df['Wednesday'])

p = round(p, 6)
f = round(f, 2)

statanswers = [f, p, k, N]
statnames = ['F', 'P-value', 'Unique Groups', 'Total Tweets Analyzed']

fig = plt.figure(1, figsize=(6, 10))
plt.subplot(2,1,1)
plt.boxplot([satcleanscores.values, suncleanscores, moncleanscores, tuescleanscores, wedscleanscores], notch=True)
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
plt.axhline(y=0, lw=0.5, ls='dashed')
plt.ylabel('Sentiment Score')
plt.title('John Cena Sentiment Scores')

table1 = plt.table(cellText=[NValueslist], colLabels=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'], loc='bottom', cellLoc='center', rowLabels=['N'])
table1.auto_set_font_size(False)
table1.set_fontsize(10)

plt.subplot(2,1,2)
table2 = plt.table(label=['ANOVA'], cellText=[statanswers], loc='center', cellLoc='center', colLabels=['F', 'P-value', 'Unique Groups', 'Total N'])
plt.axis('off')

table2.auto_set_font_size(False)
table2.set_fontsize(10)

plt.tight_layout(h_pad=-10)

plt.savefig('John Cena Sentiment Score Boxplots with ANOVA.png')

plt.show()