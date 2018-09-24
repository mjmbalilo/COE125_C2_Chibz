# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Airline Reservation System\admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gbFlightDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.gbFlightDetails.setGeometry(QtCore.QRect(20, 20, 821, 621))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gbFlightDetails.setFont(font)
        self.gbFlightDetails.setObjectName("gbFlightDetails")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.gbFlightDetails)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 50, 351, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2000, 9, 14))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.gbFlightDetails)
        self.label.setGeometry(QtCore.QRect(20, 300, 91, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.gbFlightDetails)
        self.listWidget.setGeometry(QtCore.QRect(20, 340, 211, 271))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.gbFlightDetails)
        self.label_2.setGeometry(QtCore.QRect(250, 340, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.gbFlightDetails)
        self.label_3.setGeometry(QtCore.QRect(250, 380, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.gbFlightDetails)
        self.label_4.setGeometry(QtCore.QRect(250, 420, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.gbFlightDetails)
        self.label_5.setGeometry(QtCore.QRect(250, 460, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.gbFlightDetails)
        self.label_6.setGeometry(QtCore.QRect(250, 500, 141, 31))
        self.label_6.setObjectName("label_6")
        self.gbFlightDetails_2 = QtWidgets.QGroupBox(self.gbFlightDetails)
        self.gbFlightDetails_2.setGeometry(QtCore.QRect(520, 20, 281, 581))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gbFlightDetails_2.setFont(font)
        self.gbFlightDetails_2.setObjectName("gbFlightDetails_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.gbFlightDetails_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 30, 241, 531))
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gbFlightDetails.setTitle(_translate("MainWindow", "Flight Details"))
        self.label.setText(_translate("MainWindow", "Flights:"))
        self.label_2.setText(_translate("MainWindow", "Location:"))
        self.label_3.setText(_translate("MainWindow", "Departure:"))
        self.label_4.setText(_translate("MainWindow", "Arrival:"))
        self.label_5.setText(_translate("MainWindow", "Price:"))
        self.label_6.setText(_translate("MainWindow", "Available Seats:"))
        self.gbFlightDetails_2.setTitle(_translate("MainWindow", "Passengers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

