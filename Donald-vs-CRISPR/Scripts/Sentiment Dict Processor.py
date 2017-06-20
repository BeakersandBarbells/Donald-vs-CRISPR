import pandas as pd
import json

doc = open('C:\Users\m144851\Dropbox\Personal\Education\Independent Learning\Data Science\Projects\CRISPR Sentiment\AFINN-en-165.txt', 'r')

scores = {}
for line in doc:
    term, score = line.split("\t")
    scores[term] = int(score)

output = open('SentimentDict.json','w')

json.dumps(scores, output)

# print scores
#
# df = pd.DataFrame.from_dict(scores, orient='index')
# df.columns = ['Score']
# df.index.name = 'Word'
# df = df.sort_index(axis=0, ascending=True)
#
# print df.head()

#for line in doc:
    #print (line)