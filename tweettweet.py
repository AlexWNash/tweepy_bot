import time

import tweepy

auth = tweepy.OAuthHandler('dtkeC5gCBOctt3DAitmSG3gJr', 'f9ppbcs5hpKbPKh7jQpI3600N52oun4o5kvTYx8wGDIYWu3uAy')
auth.set_access_token('1428373022-sWby3sr3Uf8lAMdizTkIGxE0BFmcBP4M9gdsRD4',
                      'lbzo5A387iiIuG3iVaC0ooZyjriHmbDP8r898tVbdfMJ3')

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
