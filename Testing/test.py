# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mapua\COE\COE125\test\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FlightReservation(object):
    def setupUi(self, FlightReservation):
        FlightReservation.setObjectName("FlightReservation")
        FlightReservation.resize(400, 300)
        self.Login = QtWidgets.QPushButton(FlightReservation)
        self.Login.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.Login.setObjectName("Login")
        self.Signup = QtWidgets.QPushButton(FlightReservation)
        self.Signup.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.Signup.setObjectName("Signup")
        self.titlelbl = QtWidgets.QLabel(FlightReservation)
        self.titlelbl.setGeometry(QtCore.QRect(110, 60, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titlelbl.setFont(font)
        self.titlelbl.setObjectName("titlelbl")
        self.usernamelbl = QtWidgets.QLabel(FlightReservation)
        self.usernamelbl.setGeometry(QtCore.QRect(50, 100, 47, 13))
        self.usernamelbl.setObjectName("usernamelbl")
        self.lbl = QtWidgets.QLabel(FlightReservation)
        self.lbl.setGeometry(QtCore.QRect(50, 150, 47, 13))
        self.lbl.setObjectName("lbl")
        self.usernaametext = QtWidgets.QLineEdit(FlightReservation)
        self.usernaametext.setGeometry(QtCore.QRect(50, 120, 113, 20))
        self.usernaametext.setObjectName("usernaametext")
        self.lineEdit_2 = QtWidgets.QLineEdit(FlightReservation)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 180, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(FlightReservation)
        QtCore.QMetaObject.connectSlotsByName(FlightReservation)

    def retranslateUi(self, FlightReservation):
        _translate = QtCore.QCoreApplication.translate
        FlightReservation.setWindowTitle(_translate("FlightReservation", "Dialog"))
        self.Login.setText(_translate("FlightReservation", "Login"))
        self.Signup.setText(_translate("FlightReservation", "Signup"))
        self.titlelbl.setText(_translate("FlightReservation", "Flight Reservation"))
        self.usernamelbl.setText(_translate("FlightReservation", "Username"))
        self.lbl.setText(_translate("FlightReservation", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FlightReservation = QtWidgets.QDialog()
    ui = Ui_FlightReservation()
    ui.setupUi(FlightReservation)
    FlightReservation.show()
    sys.exit(app.exec_())

