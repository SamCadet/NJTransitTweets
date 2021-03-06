# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NJTransitTweetsUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 482)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 440))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(10, 80, 600, 41))
        self.dateLabel.setObjectName("dateLabel")
        self.stationLabel = QtWidgets.QLabel(self.centralwidget)
        self.stationLabel.setGeometry(QtCore.QRect(10, 200, 600, 31))
        self.stationLabel.setObjectName("stationLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(10, 310, 141, 61))
        self.submitButton.setObjectName("submitButton")
        self.NJTransitTweetsLabel = QtWidgets.QLabel(self.centralwidget)
        self.NJTransitTweetsLabel.setGeometry(QtCore.QRect(280, 10, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NJTransitTweetsLabel.setFont(font)
        self.NJTransitTweetsLabel.setObjectName("NJTransitTweetsLabel")
        self.dateTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateTextEdit.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.dateTextEdit.setObjectName("dateTextEdit")
        self.stationTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stationTextEdit.setGeometry(QtCore.QRect(10, 260, 191, 31))
        self.stationTextEdit.setObjectName("stationTextEdit")
        self.tweetScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.tweetScrollArea.setGeometry(QtCore.QRect(620, 90, 431, 281))
        self.tweetScrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.tweetScrollArea.setWidgetResizable(True)
        self.tweetScrollArea.setObjectName("tweetScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 427, 277))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tweetsDisplayTextEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.tweetsDisplayTextEdit.setGeometry(QtCore.QRect(0, 0, 431, 281))
        self.tweetsDisplayTextEdit.setObjectName("tweetsDisplayTextEdit")
        self.tweetScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateLabel.setText(_translate("MainWindow", "<html><head/><body><p>Enter today\'s date in YYYY-MM-DD format including hyphens:</p></body></html>"))
        self.stationLabel.setText(_translate("MainWindow", "Enter the station(s) to find more info, press q to quit:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.NJTransitTweetsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NJ Transit Tweets</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
