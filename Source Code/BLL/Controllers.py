# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Signup import Ui_SignupWindow
from Views.Admin import Ui_AdminWindow
from Views.Customer import Ui_CustomerWindow
from Views.Login import Ui_LoginWindow
from Models import Users, Flights, Passengers, Payments

class Ui_Controllers:
    
    def Login(self):
        self.LoginWindow = QtWidgets.QDialog()
        self.LoginUi = Ui_LoginWindow()
        self.LoginUi.setupUi(self.LoginWindow, self.LoginClicked, self.LoginSignUpClicked)
        self.LoginWindow.show()
        #self.Admin()
    def Customer(self, userID):
        self.CustomerWindow = QtWidgets.QDialog()
        self.CustomerUi = Ui_CustomerWindow()
        self.CustomerUi.setupUi(self.CustomerWindow)
        self.CustomerUi.setUserID(userID)
        self.CustomerWindow.show()  
    def Signup(self):
        self.SignUpWindow = QtWidgets.QDialog()
        self.SignupUi = Ui_SignupWindow()
        self.SignupUi.setupUi(self.SignUpWindow, self.SignUpClicked)
        self.SignUpWindow.show()
    def Admin(self):
        ctr = Controllers()
        self.AdminWindow = QtWidgets.QDialog()
        self.AdminUi = Ui_AdminWindow()
        self.AdminUi.setupUi(self.AdminWindow, self.DateFlightsClicked, ctr.UsersLoad, self.ListUsersClicked, self.DeleteUserClicked)
        self.AdminWindow.show()
    def ShowWindow(self, window, userID = None):
        if window == "ADMIN":
            self.Admin()
        elif window == "SIGNUP":
            self.Signup()
        elif window == "CUSTOMER":
            self.Customer(userID)
        elif window == "LOGIN":
            self.Login()
    def MessageBox(self,message,isSuccess):
        self.msgBox = QtWidgets.QMessageBox()
        if isSuccess is True:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.setWindowTitle('Successful!')
        else:
            self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            self.msgBox.setWindowTitle('Warning!')
        self.msgBox.setText(message)
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msgBox.exec_()
    
    #region Login
    def LoginClicked(self):
        try:
            loginCtr = Controllers()
            loginCtr.LoginCheck(self.LoginUi.txtUsername.text(), self.LoginUi.txtPassword.text())
        
            if loginCtr.HasError is True:
                self.MessageBox(loginCtr.ErrorMessage, False)
            else:
                self.ShowWindow(loginCtr.Window)
        except Exception as e:
            print(str(e))
    def LoginSignUpClicked(self):
        self.ShowWindow("SIGNUP")
        self.LoginWindow.hide()
    def SignUpClicked(self):
        signupCtr = Controllers()
        userInfo = []
        userInfo.append(self.SignupUi.txtFN.text())
        userInfo.append(self.SignupUi.txtLN.text())
        userInfo.append(self.SignupUi.txtEmail.text())
        userInfo.append(self.SignupUi.txtUsername.text())
        userInfo.append(self.SignupUi.txtPassword.text())
        userInfo.append(self.SignupUi.txtAddress1.text() + self.SignupUi.txtAddress2.text())
        userInfo.append(self.SignupUi.dateBirth.text())
        userInfo.append(str(self.SignupUi.cbGender.currentText()))
        userInfo.append(self.SignupUi.txtContactNum.text())
        signupCtr.SignUpCheck(userInfo)
        if signupCtr.HasError is True:
            self.MessageBox(signupCtr.ErrorMessage, False)
        else:
            self.MessageBox('Your account has been successfully created!', True)
            self.SignUpWindow.close()
            self.LoginWindow.show()

    #endregion

    #region Admin

    def ListUsersClicked(self, item):
        userModel = Users()
        userModel.FindUser(item.text())
        user = userModel.User
        self.AdminUi.lblUsername.setText(item.text())
        self.AdminUi.lblUserFName.setText(user[1])
        self.AdminUi.lblUserLName.setText(user[2])
        self.AdminUi.lblEmail.setText(user[3])
        self.AdminUi.lblAddress.setText(user[6])
        self.AdminUi.lblBirthDate.setText(user[7])
        self.AdminUi.lblUserGender.setText(user[8])
        self.AdminUi.lblNum.setText(user[9])
    def DeleteUserClicked(self):
        userModel = Users()
        userModel.FindUser(self.AdminUi.lblUsername.text())
        userModel.DeleteUser(userModel.User[0])

        listItems = self.AdminUi.lstUsers.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.AdminUi.lstUsers.takeItem(self.AdminUi.lstUsers.row(item))

    def DateFlightsClicked(self, date):
        print(date.toString())
    # def DeleteFlightClicked(self):
    # def UpdateFlightClicked(self):
    # def DeletePassengerClicked(self):

    #endregion


class Controllers:
    __window = None
    __userID = None
    __hasError = False
    __errorMessage = None

    @property
    def Window(self):
        return self.__window
    @property
    def UserID(self):
        return self.__userID
    @property
    def HasError(self):
        return self.__hasError
    @property
    def ErrorMessage(self):
        return self.__errorMessage

    def LoginCheck(self, username, password):
        adminUsername = "admin"
        adminPassword = "admin"
        
        try:
            if not (username and password):
                raise Exception('Please fill up the required fields!')

            userModel = Users()
            userModel.FindUser(username, password)
            user = userModel.User  
            if user is not None:
                global userID
                userID = user[0]
                self.__window = "CUSTOMER"
                self.__userID = userID
                self.__hasError = False        
            elif (username == adminUsername) and (password == adminPassword):
                self.__window = "ADMIN"
                self.__hasError = False
            else:
                raise Exception('Invalid Username and Password')
        except Exception as e:
            self.__hasError = True
            self.__errorMessage = str(e)

    def SignUpCheck(self, userInfo):
        try:
            for info in userInfo:
                if info is '':
                    raise Exception('Please fill up the required fields!')
            
            userModel = Users()
            userModel.AddUser(tuple(userInfo))
            if userModel.HasError is True:
                raise Exception(userModel.ErrorMessage)
            
        except Exception as e:
            self.__hasError = True
            self.__errorMessage = str(e)                             

    # def FlightsLoad(self):   
    # def FlightDetailsLoad(self):
    # def PassengersLoad(self):

    @property
    def UsersLoad(self):
        userModel = Users()
        userModel.ViewAllUser()
        self.userLoad = userModel.AllUser
        return self.userLoad
    
    @property
    def UserLoad(self, username):
        userModel = Users()
        userModel.FindUser(username)
        return userModel.User