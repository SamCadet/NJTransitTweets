import tweepy
import os
import re
import sys

from NJTransitTweets_Ui import Ui_MainWindow

from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui


# NJTransitTweets - reveal Twitter updates on late trains with a simple search

consumerkey = os.environ['TWITTER_API_KEY']
consumerSecret = os.environ['TWITTER_API_SECRET_KEY']
accessToken = os.environ['TWITTER_ACCESS_TOKEN']
accessTokenSecret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=False,
                 wait_on_rate_limit_notify=False)

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('NJ Transit Tweets')
        self.dateTextEdit
        self.dateButton.clicked.connect(self.buttonPushed)
        self.stationTextEdit
        self.stationButton.clicked.connect(self.buttonPushed)
        self.submitButton.clicked.connect(self.NJTransitTweets)

    def NJTransitTweets(userDate, userStation):

        njtTweets = tweepy.Cursor(api.search, q="NJTransit",
                                  until=userDate, count=100).items()

        omitWords = ['Bus', 'bus', 'Shuttle', 'shuttle', 'Bike', 'bike']
        neededWords = ['Late', 'late', 'Cancel', 'cancel',
                       'Cancelled', 'cancelled', 'Delay', 'delay', 'Delays', 'delays', 'Weather', 'weather', 'Flood', 'flood', 'Mechanical', 'mechanical']

        counter = 0

        # userDate = input(
        #     'Enter today\'s date in YYYY-MM-DD format including hyphens: ')

        # userStation = input(
        #     'Enter the station(s) to find more info, press q to quit: ')

        userDate = self.dateTextEdit.text()
        userStation = self.stationTextEdit.text()

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

    def buttonPushed(self):
        self.returnPressed.connect(self.onClick)


# NJTransitTweets(userDate, userStation)


if __name__ == '__main__':
    app = qtw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()

    sys.exit(app.exec_())
