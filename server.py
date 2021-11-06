<<<<<<< HEAD
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
=======
import requests
import os
import json
import sys
from datetime import datetime

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_token_here>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # created_at = datetime.strptime(response_line[0]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            print(json.dumps(json_response, indent=4, sort_keys=True))
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

sys.stdout = open('tweet4.txt', mode='w', encoding='utf-8')
>>>>>>> c0a1a69a1e09d3798e4a7f34dc9aacf50896fc93

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
