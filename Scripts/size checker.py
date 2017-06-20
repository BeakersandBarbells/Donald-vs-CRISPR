import datetime
import os
import time
from datetime import datetime

t = os.stat('C:\Users\m144851\Desktop\CRISPR Sentiment\DJTTweets2017-06-17+00.json')
#C = os.stat('C:\Users\m144851\Desktop\CRISPR Sentiment\CRISPRTweets2017-06-16+00.csv')
#M = os.stat('C:\Users\m144851\Desktop\CRISPR Sentiment\MysteryChallengerTweets2017-06-16+00.csv')

trumpcreation0 = datetime.fromtimestamp(t.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

print trumpcreation0

trump = t.st_size
#CRISPR = C.st_size
##MysteryChallenger = M.st_size

starttime = datetime(2017, 06, 17, 10, 01, 00)

now = datetime.now()

hourspassed = round((((now - starttime).total_seconds())/60/60), 2)

timeleft = 7 * 24

print "Hours since start (1:26PM on the 15th): " + str(hourspassed) + '\n'

print 'Trump tweet file size since start: '+str(trump/1000)+' KB'
print 'Trump bytes/hour: '+str(round(trump/hourspassed, 2))
#print 'CRISPR bytes/hour: '+str(round(CRISPR/hourspassed, 2))
#print 'Mystery Challenger bytes/hour: '+str(round(MysteryChallenger/hourspassed, 2)) + '\n'

#print 'Fun Fact #1 - so far there are ' + str(trump/1000 / (CRISPR/1000)) + ' Trump tweets per CRISPR tweet.' + '\n'

print 'Projected space needed to hold all Trump Tweets for a week: ' + str(round((timeleft * round(trump/hourspassed, 2))/(1000**2), 2)) + 'MB'