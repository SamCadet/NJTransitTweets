import tweepy
import os
import time

# NJTransitTweets - reveal Twitter updates on late trains with a simple search

consumerkey = os.environ['TWITTER_API_KEY']
consumerSecret = os.environ['TWITTER_API_SECRET_KEY']
accessToken = os.environ['TWITTER_ACCESS_TOKEN']
accessTokenSecret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=False,
                 wait_on_rate_limit_notify=False)


njtTweets = tweepy.Cursor(api.search, q="NJ Transit",
                          until="2021-07-20", count=200).items()

omitWords = ['Bus', 'bus', 'Shuttle', 'shuttle', 'Bike', 'bike']
neededWords = ['Late', 'late', 'Cancel', 'cancel',
               'Cancelled', 'cancelled', 'Delay', 'delay', 'Delays', 'delays', 'Weather', 'weather', 'Flood', 'flood', 'Mechanical', 'mechanical']


def NJTransitTweets(userStation):
    counter = 0
    for tweet in njtTweets:
        if any([word in tweet.text for word in omitWords]):
            continue
        if userStation.capitalize() in tweet.text and any([word in tweet.text for word in neededWords]):
            print(str(tweet.text) + '\n')
            counter += 1
        if counter == 50:
            print('Search complete, have a good day.')
            break
        elif userStation == 'q':
            print('OK, have a good day.')
            break


userStation = input(
    'Enter the station(s) to find more info, press q to quit: ')

NJTransitTweets(userStation)
