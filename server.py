"""
File: server.py
Name: Group
---------------------------
This file reads all the tweets from Twitter and write 
each tweet’s text and timestamp to tweets.txt in the
following format:

tweet timestamp in YYYY-MM-DD-HH-MM-SS format, tweet text
"""
import tweepy


consumer_key = '55iKh2vnoNjRNldmBRi1SAT3e'
consumer_secret = 'eFIqDQn8mkf0jaXB1PUgtjPHWmDqLewFJTJMVHdxkhcdrgPVKe'
access_key= '1435726675925405696-rPMEdVKvBBAIMVSWqioNfdf9Rlq0ef'
access_secret = 'NJAhAqMjYIyoAevVA7t8QWiboX1LVBwr513xNBTRokSyE'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
 
api = tweepy.API(auth)

 

def main():
	"""
	Read tweet and write to .txt
	"""
	with open('tweets.txt', 'w') as out:
			out.write('timestamp,text\n')
			for tweet in tweepy.Cursor(api.search_tweets, q='*', lang='en').items():
				timestamp = str(tweet.created_at)
				text = tweet.text
				out.write(timestamp+','+text+'\n')


if __name__ == '__main__':
    main()

