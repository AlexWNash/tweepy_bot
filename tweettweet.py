import time

import tweepy

auth = tweepy.OAuthHandler()
auth.set_access_token()

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'Python'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# # Generous Bot
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)
