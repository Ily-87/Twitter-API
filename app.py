if __name__ == '__main__':
    app.run(debug=True)

import tweepy

API_KEY = "W3f0s2G3CYQgI6WOjfrD7xOSx"
API_SECRET = "gSpCfHHKk4hMtqbyhHXoQMO51HLNzsNHVGYawc3WYN6WRF1Q0c"
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

import sys
import jsonpickle
import os
import json
import re

from flask import jsonify
from django.http import JsonResponse
from flask import Flask
import pprint
app = Flask(__name__)

@app.route('/')
def function():

    return jsonify(results)

searchQuery = 'eigen bedrijf'  # this is what we're searching for
maxTweets = 2 # Some arbitrary large number
tweetsPerQry = 1  # this is the max the API permits
sinceId = None
max_id = -1
tweetCount = 0
tweets_data_path = "tweets.json"
results = []



    # tweets_file = json.dumps(tweets_data_path)
    # regex = "\"created_at\": \"(\w+ (?:Jan|Feb|Aug|Sep|Oct|Nov|Dec) \d+ [\d:]+ \+\d+ 201[89])\".*? \"screen_name\": \"(\w+)\""
    #         # print(json.loads(m, indent=2))




while (tweetCount < maxTweets):

   print('The count is:', tweetCount)
   # tweetCount += 1
   if (max_id <= 0):
       if (not sinceId):
           results = api.search(q=searchQuery, count=tweetsPerQry)

   for tweet in results:
       # print(tweet)
       tweetCount += 1
print("Good bye!")

def read_json(tweets_data_path):
    tweets_file = open(tweets_data_path, "r")

    regex = "(screen_name\W+\w+)|(created_at\W+\w+\s(Feb|Jan|Aug|Sep|Oct|Nov|Dec)\s\d+\s\d+\D\d\d\D\d\d\s\D\d+\s(2018|2019))"
    for tweet_line in tweets_file:

        tweet_line = results.append(tweet_line)
    # print(type(m))

    # tweet = re.findall(regex, tweet)
    # print(tweet)
    return tweet
results = read_json(tweets_data_path)
