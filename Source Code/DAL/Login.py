# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):

    #Intialization
    def setupUi(self, Dialog, LoginClicked = None, SignUpClicked = None):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 379)
        self.lblTitle = QtWidgets.QLabel(Dialog)
        self.lblTitle.setGeometry(QtCore.QRect(50, 30, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(50, 290, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnSignUp = QtWidgets.QPushButton(Dialog)
        self.btnSignUp.setGeometry(QtCore.QRect(260, 290, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setObjectName("btnSignUp")
        self.lblUsername = QtWidgets.QLabel(Dialog)
        self.lblUsername.setGeometry(QtCore.QRect(50, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(Dialog)
        self.lblPassword.setGeometry(QtCore.QRect(50, 190, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.txtUsername = QtWidgets.QLineEdit(Dialog)
        self.txtUsername.setGeometry(QtCore.QRect(50, 140, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtUsername.setFont(font)
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        self.txtPassword.setGeometry(QtCore.QRect(50, 220, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtPassword.setFont(font)
        self.txtPassword.setObjectName("txtPassword")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        ######################### Button Event ###############################
        self.btnLogin.clicked.connect(LoginClicked)
        self.btnSignUp.clicked.connect(SignUpClicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Flight Reservation System"))
        self.lblTitle.setText(_translate("Dialog", "<html><head/><body><p>FLIGHT RESERVATION</p><p><br/></p></body></html>"))
        self.btnLogin.setText(_translate("Dialog", "Login"))
        self.btnSignUp.setText(_translate("Dialog", "Sign Up"))
        self.lblUsername.setText(_translate("Dialog", "Username:"))
        self.lblPassword.setText(_translate("Dialog", "Password:"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_LoginWindow()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

