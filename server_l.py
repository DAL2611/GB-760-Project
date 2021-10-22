import requests
import os
import json
import sys
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


def connect_to_endpoint(ls, url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    #print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            # created_at = datetime.strptime(response_line[0]['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
            ls.append(json.dumps(json_response, indent=4, sort_keys=True))
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

def write(output):
    with open('tweets2', 'w') as out:
         for tweet in output:
             print(tweet)
             out.write(tweet)
   
            


def main():
    url = create_url()
    timeout = 0
    ls = []
    while True:
        output = connect_to_endpoint(ls, url)
        timeout += 1
    print(ls)
    write(output)


if __name__ == "__main__":
    main()
