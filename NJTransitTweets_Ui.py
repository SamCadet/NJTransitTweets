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
        MainWindow.resize(920, 400)
        MainWindow.setMinimumSize(QtCore.QSize(920, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dateTextEdit.setGeometry(QtCore.QRect(10, 140, 191, 31))
        self.dateTextEdit.setObjectName("dateTextEdit")
        self.stationTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.stationTextEdit.setGeometry(QtCore.QRect(10, 240, 191, 31))
        self.stationTextEdit.setObjectName("stationTextEdit")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(10, 80, 621, 41))
        self.dateLabel.setObjectName("dateLabel")
        self.stationLabel = QtWidgets.QLabel(self.centralwidget)
        self.stationLabel.setGeometry(QtCore.QRect(10, 200, 571, 41))
        self.stationLabel.setObjectName("stationLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(10, 310, 141, 61))
        self.submitButton.setObjectName("submitButton")
        self.NJTransitTweetsLabel = QtWidgets.QLabel(self.centralwidget)
        self.NJTransitTweetsLabel.setGeometry(QtCore.QRect(230, 0, 450, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NJTransitTweetsLabel.setFont(font)
        self.NJTransitTweetsLabel.setObjectName("NJTransitTweetsLabel")
        self.tweetListView = QtWidgets.QListView(self.centralwidget)
        self.tweetListView.setGeometry(QtCore.QRect(640, 90, 256, 281))
        self.tweetListView.setObjectName("tweetListView")
        self.dateButton = QtWidgets.QPushButton(self.centralwidget)
        self.dateButton.setGeometry(QtCore.QRect(210, 140, 81, 31))
        self.dateButton.setObjectName("dateButton")
        self.stationButton = QtWidgets.QPushButton(self.centralwidget)
        self.stationButton.setGeometry(QtCore.QRect(210, 240, 81, 31))
        self.stationButton.setObjectName("stationButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 21))
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
        self.dateLabel.setText(_translate(
            "MainWindow", "<html><head/><body><p>Enter today\'s date in YYYY-MM-DD format including hyphens:</p></body></html>"))
        self.stationLabel.setText(_translate(
            "MainWindow", "Enter the station(s) to find more info, press q to quit:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.NJTransitTweetsLabel.setText(
            _translate("MainWindow", "NJ Transit Tweets"))
        self.dateButton.setText(_translate("MainWindow", "Enter"))
        self.stationButton.setText(_translate("MainWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
