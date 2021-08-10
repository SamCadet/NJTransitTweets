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
        self.userDate = str(self.dateTextEdit.text())
        self.userStation = str(self.stationTextEdit.text())
        self.submitButton.setAutoDefault(True)
        self.submitButton.clicked.connect(self.submitButtonPushed)

    def NJTransitTweets(self, userDate, userStation):

        njtTweets = tweepy.Cursor(api.search, q="NJTransit",
                                  until=self.userDate, count=100).items()

        omitWords = ['Bus', 'bus', 'Shuttle', 'shuttle', 'Bike', 'bike']
        neededWords = ['Late', 'late', 'Cancel', 'cancel',
                       'Cancelled', 'cancelled', 'Delay', 'delay', 'Delays', 'delays', 'Weather', 'weather', 'Flood', 'flood', 'Mechanical', 'mechanical']

        counter = 0

        # userDate = self.userDate
        # userDate = input(
        #     'Enter today\'s date in YYYY-MM-DD format including hyphens: ')
        # userStation = self.userStation

        # userStation = input(
        #     'Enter the station(s) to find more info, press q to quit: ')

        for tweet in njtTweets:
            if any([word in tweet.text for word in omitWords]):
                continue
            if self.userStation.capitalize() in tweet.text and any([word in tweet.text for word in neededWords]):
                print(str(tweet.text) + '\n')
                counter += 1
            if counter > 10:
                print('Search complete, have a good day.')
                break
            elif (bool(re.match('^[0-9_-]*$', self.userDate))) is False:
                print('That\'s not a valid user date, try again.')
            elif self.userStation == 'q':
                print('OK, have a good day.')
                break

    # def dateButtonPushed(self):
    #     print('OK')

    # def stationButtonPushed(self):
    #     print('OK')

    def submitButtonPushed(self):
        return self.NJTransitTweets(self.userDate, self.userStation)


# NJTransitTweets(userDate, userStation)


if __name__ == '__main__':
    app = qtw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()

    sys.exit(app.exec_())
