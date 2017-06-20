from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime
import sys
import os

ckey = '3RrH4p6oiU80N8Pcgi1nxnioL'
csecret = 'f4yKhNRrXvjMWfG0fBbTccKhmejtuEgkncW4sryXZ4jKzx8XXi'
atoken = '209299529-ugg0BaXKF2orjzzko87p9u85Mx5rEOiK3kYp9Jy4'
asecret = 'G448bf2rDy6LKabSb17yOUgib67yVZi54UxP5h4tCReUU'

todaydate = datetime.datetime.now().date()

print datetime.datetime.now()

class listener(StreamListener):
    def __init__(self, directory='', filename='DJTTweets' + str(todaydate), max_files=sys.maxint, max_file_size=500000000):
        self.ii = 0
        self.directory, self.filename       = directory, filename
        self.max_file_size, self.max_files  = max_file_size, max_files
        self.finished, self.fh              = False, None
        self.open()

    def rotate(self):
        if (os.stat(self.filename_template).st_size > self.max_file_size):
            self.close()
            self.ii += 1
            if (self.ii <= self.max_files):
                self.open()
            else:
                self.close()
                self.finished = True

    def open(self):
        self.fh = open(self.filename_template, 'w')

    def on_data(self, data):
        try:
            tweet = json.loads(data)
            userbirth = tweet['user']['created_at']
            userfollowers = tweet['user']['followers_count']
            userid = tweet['user']['id_str']
            username = tweet['user']['name']
            userstatuscount = tweet['user']['statuses_count']
            usertimezone = tweet['user']['time_zone']
            userverified = tweet['user']['verified']
            tweetcreationdate = tweet['created_at']
            tweetid = tweet['id_str']
            tweetcoords = None
            if tweet['place']:
                if tweet['place']['bounding_box']:
                    tweetcoords = tweet['place']['bounding_box']['coordinates']
            tweetretweets = tweet['retweet_count']
            tweettext = tweet['text']
            tweethashtags = None
            if tweet['entities']:
                if tweet['entities']['hashtags']:
                    if tweet['entities']['hashtags']['text']:
                        tweethashtags = tweet['entities']['hashtags']['text']
            tweetfavorites = tweet['favorite_count']

            dataout = {'UserID': userid, 'Username': username, 'UserBirth': userbirth, 'Userfollowers': userfollowers,
                   'UserTweetCount': userstatuscount, 'Usertimezone': usertimezone, 'Verified': userverified, 'TweetCreationDate':tweetcreationdate,
                   'TweetID': tweetid, 'Tweettext': tweettext, 'Hashtags': tweethashtags, 'Coordinates': tweetcoords,
                   'Favorites': tweetfavorites, 'Retweets': tweetretweets}

            if tweet['lang'] == 'en':
                out = json.dumps(dataout, separators=(',', ':'))
                self.fh.write(out + '\n')


        except:
            pass

        self.fh.flush()
        self.rotate()

    def close(self):
        self.fh.close()

    @property
    def filename_template(self):
        return self.directory + self.filename + "+%0.2d.json" % self.ii

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Donald Trump"])