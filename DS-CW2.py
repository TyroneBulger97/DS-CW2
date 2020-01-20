import twitter,json,csv

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# setup a file to write to
csvfile = open('WWIII_tweets_delimiter.csv', 'a+')
csvwriter = csv.writer(csvfile, delimiter='|')

#  heres a function that takes out characters that can break
#  our import into Excel and replaces them with spaces
#  it also does the unicode bit
def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val.encode('utf-8')
    return clean


q = "#Monarchy" # Comma-separated list of terms can go here
print 'Filtering the public timeline for track="%s"' % (q,)

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

for tweet in stream:
    # write the values to file
    csvwriter.writerow([tweet['created_at'],
    getVal(tweet['user']['screen_name']),
    tweet['user']['created_at'],
    tweet['user']['follower_count']
])
    ([tweet['user']['screen_name'].encode('utf-8'),tweet['text'].encode('utf-8')])
    # print something to the screen, mostly so we can see what is going on...
    print tweet['user']['screen_name'].encode('utf-8'), tweet['text'].encode('utf-8')
