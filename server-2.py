import requests
import os
import json
from datetime import datetime

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_token_here>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    return "https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=created_at"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    # print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            text = str(json_response)
            # print(json_response)
            # created_at = datetime.strptime(response_line[0]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    tweet.write(text)
    
    
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
        
def connect_to_endpoint_2(url):
	response = requests.get(url)
	print(response['created_at'])

def main():
    tweet = open('tweet.txt', 'r+')
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()
