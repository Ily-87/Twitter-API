import tweepy

# Replace the API_KEY and API_SECRET with your application's key and secret.

API_KEY = "SMvmRlgbZjz8dMNM6LsgbYbfi"
API_SECRET = "BjQpi0BOP4k0Et1YRToVeIj02jQBZWFFudYsRTPOrnz14Lk6hN"
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code
import sys
import jsonpickle
import os

#
searchQuery = 'eigen begonnen'  # this is what we're searching for
maxTweets = 1000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets.txt' # We'll store the tweets in a text file.
#
#
# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None
#
# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)

                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepyError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

            print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))






# import json
# from pprint import pprint
# dict1 = {}
# dict2 = {}
# def js_r(tweets):
# #    with open(tweets) as js_r:
# #        # return(json.load(f_in))
# #
# #        return(json.loads(json.dumps([])))
# #        [{}, {}]
# #        return json.loads(json.loads(get_info))
# #        return(json.load(f_in))
# #        result = json.loads(output)
# #        print(result)
# #        print(result['contributors'])
#     with open('tweets.json') as f:
#
# 		#print json to a string
#         return(json.loads(json.dumps([])))
#         [{}, {}]
#
#         result = json.load(f)
#         print("user")
#
# if __name__ == "__main__":
#
#     my_data = js_r('tweets.json')
#     print(my_data)
#


# import json
# import os
#
# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, 'tweets.json')
# with open("tweets.json",'r') as fi:
# 	pass
# 	tweets = json.loads(json.dumps('tweets.json'))
# 	for tweet in tweets:
# 		print(tweets)
# print(fi)


# def dump(obj):
# 	for attr in dir('tweets.json'):
# 		print("obj.%s = %r" % (attr, getattr(obj, attr)))
