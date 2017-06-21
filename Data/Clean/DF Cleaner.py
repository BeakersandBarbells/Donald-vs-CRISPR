import pandas as pd
import simplejson

#this script opens two different JSON docs from my tweet streamers, compiles them into a big list, converts to a dataframe, then dumps them into a .pkl file. Neat!

rawdata1 = open('C:\Users\m144851\Desktop\Github '
                'Projects\Donald-vs-CRISPR\Data\Raw\DJTTweets2017-06-17+00.json').read()

dict_list1 = [d.strip() for d in rawdata1.splitlines()]

tweetlist = []

for line in (dict_list1):
    try:
        a = simplejson.loads(line)
        tweetlist.append(a)
    except:
        pass

df = pd.DataFrame(tweetlist)

df.to_pickle('AllDJTTweetsdataframe.pkl')