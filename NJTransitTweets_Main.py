import tweepy
import os
import re
import sys
from NJTransitTweets_Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets as qtw


# NJTransitTweets - reveal Twitter updates on late trains with a simple search

consumerkey = os.environ['TWITTER_API_KEY']
consumerSecret = os.environ['TWITTER_API_SECRET_KEY']
accessToken = os.environ['TWITTER_ACCESS_TOKEN']
accessTokenSecret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth, wait_on_rate_limit=False,
                 wait_on_rate_limit_notify=False)

class GatherTweets(QtCore.QObject):

    tweetsFound = QtCore.pyqtSignal(str)

    def write(self, text):
        self.tweetsFound.emit(str(text))

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('NJ Transit Tweets')
        self.userDate = self.dateTextEdit.setText('YYYY-MM-DD')
        self.userStation = self.stationTextEdit.setText(
            'Ex. Newark Broad Street, Northeast Corridor etc.')
        self.submitButton.setAutoDefault(True)
        self.submitButton.clicked.connect(self.submitButtonPushed)
        sys.stdout = GatherTweets(tweetsFound=self.displayTweets)

    def displayTweets(self, text):
        self.tweetsDisplayTextEdit.append(text)

    def NJTransitTweets(self, userDate, userStation):

        njtTweets = tweepy.Cursor(api.search, q="NJTransit",
                                  until=self.userDate, count=100).items()

        omitWords = ['Bus', 'bus', 'Shuttle', 'shuttle', 'Bike', 'bike']
        neededWords = ['Late', 'late', 'Cancel', 'cancel',
                       'Cancelled', 'cancelled', 'Delay', 'delay', 'Delays', 'delays', 'Weather', 'weather', 'Flood', 'flood', 'Mechanical', 'mechanical']

        counter = 0

        self.userDate = str(self.dateTextEdit.text())
        self.userStation = str(self.stationTextEdit.text())

        for tweet in njtTweets:
            if any([word in tweet.text for word in omitWords]):
                continue
            if self.userStation.capitalize() in tweet.text and any([word in tweet.text for word in neededWords]):
                print(str(tweet.text) + '\n')
                counter += 1
            if counter > 3:
                print('Search complete, have a good day.')
                break
            if (bool(re.match('^[0-9_-]*$', self.userDate))) is False:
                print('That\'s not a valid user date, try again.')
                break
            elif self.userStation == 'q':
                print('OK, have a good day.')
                break

    def submitButtonPushed(self):
        print(self.NJTransitTweets(self.userDate, self.userStation))
        print(
            f'The user date is {self.userDate} and the user station/line is {self.userStation}.')
        return


if __name__ == '__main__':
    app = qtw.QApplication([])
    app.setStyle('Fusion')
    window = Window()
    window.show()

    sys.exit(app.exec_())
