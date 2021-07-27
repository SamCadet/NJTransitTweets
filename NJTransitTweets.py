import tweepy
import os
import re

# NJTransitTweets - reveal Twitter updates on late trains with a simple search

consumerkey = os.environ['TWITTER_API_KEY']
consumerSecret = os.environ['TWITTER_API_SECRET_KEY']
accessToken = os.environ['TWITTER_ACCESS_TOKEN']
accessTokenSecret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=False,
                 wait_on_rate_limit_notify=False)


def NJTransitTweets(userDate, userStation):

    njtTweets = tweepy.Cursor(api.search, q="NJ Transit",
                              until=userDate, count=100).items()

    omitWords = ['Bus', 'bus', 'Shuttle', 'shuttle', 'Bike', 'bike']
    neededWords = ['Late', 'late', 'Cancel', 'cancel',
                   'Cancelled', 'cancelled', 'Delay', 'delay', 'Delays', 'delays', 'Weather', 'weather', 'Flood', 'flood', 'Mechanical', 'mechanical']

    counter = 0

    for tweet in njtTweets:
        if any([word in tweet.text for word in omitWords]):
            continue
        if userStation.capitalize() in tweet.text and any([word in tweet.text for word in neededWords]):
            print(str(tweet.text) + '\n')
            counter += 1
        if counter > 10:
            print('Search complete, have a good day.')
            break
        elif (bool(re.match('^[0-9_-]*$', userDate))) is False:
            print('That\'s not a valid user date, try again.')
        elif userStation == 'q':
            print('OK, have a good day.')
            break


userDate = input(
    'Enter today\'s date in YYYY-MM-DD format including hyphens: ')

userStation = input(
    'Enter the station(s) to find more info, press q to quit: ')

NJTransitTweets(userDate, userStation)
