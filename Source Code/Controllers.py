# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Signup import Ui_SignupWindow
from Views.Admin import Ui_AdminWindow
from Views.Customer import Ui_CustomerWindow
from Views.Login import Ui_LoginWindow
from Models import Users, Flights, Passengers, Payments, Locations

class Ui_Controllers:
    
    #region UI
    def Login(self):
        self.LoginWindow = QtWidgets.QDialog()
        self.LoginUi = Ui_LoginWindow()
        self.LoginUi.setupUi(self.LoginWindow)
        self.SetupLoginEvents()
        self.LoginWindow.show()
    def Customer(self):
        self.CustomerWindow = QtWidgets.QDialog()
        self.CustomerUi = Ui_CustomerWindow()
        self.CustomerUi.setupUi(self.CustomerWindow)
        self.SetupCustomerEvents()
        self.CustomerWindow.show()  
    def Signup(self):
        self.SignUpWindow = QtWidgets.QDialog()
        self.SignupUi = Ui_SignupWindow()
        self.SignupUi.setupUi(self.SignUpWindow)
        self.SetupSignUpEvents()
        self.SignUpWindow.show()
    def Admin(self):
        self.AdminWindow = QtWidgets.QDialog()
        self.AdminUi = Ui_AdminWindow()
        self.AdminUi.setupUi(self.AdminWindow)
        self.SetupAdminEvents()
        self.AdminWindow.show()
    def ShowWindow(self, window):
        if window == "ADMIN":
            self.Admin()
        elif window == "SIGNUP":
            self.Signup()
        elif window == "CUSTOMER":
            self.Customer()
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
    #endregion

    #region Login
    def SetupLoginEvents(self):
        self.LoginUi.btnLogin.clicked.connect(self.LoginClicked)
        self.LoginUi.btnSignUp.clicked.connect(self.LoginSignUpClicked)
    def LoginClicked(self):
        try:
            loginCtr = Controllers()
            loginCtr.LoginCheck(self.LoginUi.txtUsername.text(), self.LoginUi.txtPassword.text())
            self.UserID = loginCtr.UserID

            if loginCtr.HasError is True:
                self.MessageBox(loginCtr.ErrorMessage, False)
            else:
                self.ShowWindow(loginCtr.Window)
        except Exception as e:
            print(str(e))
    def LoginSignUpClicked(self):
        self.ShowWindow("SIGNUP")
        self.LoginWindow.hide()
    #endregion

    #region Signup
    def SetupSignUpEvents(self):
        self.SignupUi.btnSignUp.clicked.connect(self.SignUpClicked)
        self.SignupUi.btnCancel.clicked.connect(self.SignUpCancelClicked)
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
        if (userInfo[4] != self.SignupUi.txtConfirmPassword.text()):
            self.MessageBox("Password doesn't match", False)
        elif signupCtr.HasError is True:
            self.MessageBox(signupCtr.ErrorMessage, False)
        else:
            self.MessageBox('Your account has been successfully created!', True)
            self.SignUpWindow.close()
            self.LoginWindow.show()
    def SignUpCancelClicked(self):
        self.SignUpWindow.close()
        self.LoginWindow.show()
    #endregion

    #region Admin
    def SetupAdminEvents(self):
        self.DisplayFlights()
        self.DisplayUsers()
        self.AdminUi.cbxFlightPassengers.currentIndexChanged.connect(self.CbxFlightPassengersClicked)
        self.AdminUi.lstFlights.currentItemChanged.connect(self.ListFlightsClickied)
        self.AdminUi.lstPassengers.currentItemChanged.connect(self.ListPassengersClicked)
        self.AdminUi.lstUsers.currentItemChanged.connect(self.ListUsersClicked)
        self.AdminUi.btnDeleteUser.clicked.connect(self.DeleteUserClicked)
        self.AdminUi.btnDeleteFlight.clicked.connect(self.DeleteFlightClicked)
        self.AdminUi.btnUpdateFlight.clicked.connect(self.UpdateFlightClicked)
    def DisplayFlights(self):
        flightModel = Flights()
        flightModel.ViewAllFlights()
        flightLoad = flightModel.AllFlight
        if flightLoad is not None:
            for flight in flightLoad:
                item = QtWidgets.QListWidgetItem('Flight ' + str(flight[0]))
                self.AdminUi.lstFlights.addItem(item)
                self.AdminUi.cbxFlightPassengers.addItem('Flight ' + str(flight[0]))
    def DisplayUsers(self):
        userModel = Users()
        userModel.ViewAllUser()
        userLoad = userModel.AllUser
        if userLoad is not None:
            for user in userLoad:
                item = QtWidgets.QListWidgetItem(str(user[4]))
                self.AdminUi.lstUsers.addItem(item)
    def CbxFlightPassengersClicked(self):
        passengerModel = Passengers()
        item = self.AdminUi.cbxFlightPassengers.currentText()
        passengerModel.ViewAllFlightPassengers(str(item).split()[1])
        passengerLoad = passengerModel.AllFlightPassengers
        if passengerLoad is not None:
            for passenger in passengerLoad:
                item = QtWidgets.QListWidgetItem(str(passenger[1]) + ' ' + str(passenger[2]))
                self.AdminUi.lstPassengers.addItem(item)
    def ListFlightsClickied(self, item):
        flightModel = Flights()
        flightModel.FindFlight(str(item.text()).split()[1])
        flight = flightModel.Flight
        origin = flight[1]
        destination = flight[2]
        availSeats = None
        self.AdminUi.lblOrigin.setText(origin)
        self.AdminUi.lblDestination.setText(destination)
        self.AdminUi.lblTravelDate.setText(flight[3])
        self.AdminUi.lblPrice.setText(flight[4] + ' ' + flight[5])
        self.AdminUi.lblAvailSeats.setText(availSeats)
        self.AdminUi.txtRemarks.setText(flight[6])
    def ListPassengersClicked(self, item):
        passengerModel = Passengers()
        #passengerModel.FindPassenger(passengerID)
        passenger = passengerModel.FlightPassenger
        self.AdminUi.lblFName.setText(passenger[1])
        self.AdminUi.lblLName.setText(passenger[2])
        self.AdminUi.lblGender.setText(passenger[3])
        self.AdminUi.lblAge.setText(passenger[4])
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
    def DeleteFlightClicked(self):
        flightModel = Flights()
        item = self.AdminUi.lstFlights.currentItem().text()
        flightModel.DeleteFlight(str(item).split()[1])
        listItems = self.AdminUi.lstFlights.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.AdminUi.lstFlights.takeItem(self.AdminUi.lstFlights.row(item))
    def UpdateFlightClicked(self):
        flightModel = Flights()
        item = self.AdminUi.lstFlights.currentItem().text()
        remarks = self.AdminUi.txtRemarks.text()
        flightModel.UpdateFlight(str(item).split()[1], remarks)

    #endregion

    #region Customer
    def SetupCustomerEvents(self):
        self.DisplayCountry()
        self.DisplayTime()
        self.DisplayMyFlights()
        self.DisplayUserAccount()
        self.CustomerUi.cbxOriginCountry.currentIndexChanged.connect(self.CbxOriginCountryClicked)
        self.CustomerUi.cbxDestinationCountry.currentIndexChanged.connect(self.CbxDestinationCountryClicked)
        self.CustomerUi.btnBookFlight.clicked.connect(self.BookFlightClicked)
        self.CustomerUi.btnChangePassword.clicked.connect(self.ChangePasswordClicked)
        self.CustomerUi.cbxFlights.currentIndexChanged.connect(self.CbxUserFlightsClicked)
        self.CustomerUi.lstPassengers.currentItemChanged.connect(self.ListUserPassengersClicked)
    def DisplayCountry(self):
        locationModel = Locations()
        locationModel.ViewAllCountry()
        countryLoad = locationModel.Country
        if countryLoad is not None:
            for country in countryLoad:
                self.CustomerUi.cbxOriginCountry.addItem(str(country[0]))
                self.CustomerUi.cbxDestinationCountry.addItem(str(country[0]))
    def DisplayTime(self):
        for i in range(1,25):
            self.CustomerUi.cbxTime.addItem(str(i) + ":00")
    def DisplayMyFlights(self):
        passengerModel = Passengers()
        passengerModel.ViewUserFlights(self.UserID)
        flightLoad = passengerModel.UserFlights
        if flightLoad is not None:
            for flight in flightLoad:
                self.CustomerUi.cbxFlights.addItem('Flight ' + str(flight[0]))
    def DisplayUserAccount(self):
        userModel = Users()
        userModel.FindUser(None, None, self.UserID)
        userLoad = userModel.User
        self.CustomerUi.lblUserFName.setText(userLoad[1])
        self.CustomerUi.lblUserLName.setText(userLoad[2])
        self.CustomerUi.lblEmail.setText(userLoad[3])
        self.CustomerUi.lblUsername.setText(userLoad[4])
        self.CustomerUi.lblAddress.setText(userLoad[6])
        self.CustomerUi.lblBirthDate.setText(userLoad[7])
        self.CustomerUi.lblUserGender.setText(userLoad[8])
        self.CustomerUi.lblNum.setText(userLoad[9])
    def CbxOriginCountryClicked(self):
        locationModel = Locations()
        country = self.CustomerUi.cbxOriginCountry.currentText()
        locationModel.ViewCountryCities(country)
        cityLoad = locationModel.City
        self.CustomerUi.cbxOriginCity.clear()
        if cityLoad is not None:
            for city in cityLoad:
                self.CustomerUi.cbxOriginCity.addItem(str(city[0]))
    def CbxDestinationCountryClicked(self):
        locationModel = Locations()
        country = self.CustomerUi.cbxDestinationCountry.currentText()
        locationModel.ViewCountryCities(country)
        cityLoad = locationModel.City
        self.CustomerUi.cbxDestinationCity.clear()
        if cityLoad is not None:
            for city in cityLoad:
                self.CustomerUi.cbxDestinationCity.addItem(str(city[0]))
    def BookFlightClicked(self):
        self.flightInfo = []
        self.passengerInfo = []
        locationModel = Locations()
        locationModel.ViewLocationID(self.CustomerUi.cbxOriginCountry.text(), self.CustomerUi.cbxOriginCity.text())
        originID = locationModel.LocationID
        locationModel.ViewLocationID(self.CustomerUi.cbxDestinationCountry.text(), self.CustomerUi.cbxDestinationCity.text())
        destinationID = locationModel.LocationID
        self.flightInfo.append(originID)
        self.flightInfo.append(destinationID)
        self.passengerInfo.append(self.CustomerUi.txtAdult.text())
        self.passengerInfo.append(self.CustomerUi.txtInfant.text())
        self.passengerInfo.append(self.CustomerUi.txtChildren.text())
        self.passengerInfo.append(self.CustomerUi.txtSeniorCitizen.text())
    def CbxUserFlightsClicked(self):
        passengerModel = Passengers()
        item = self.CustomerUi.cbxFlights.currentText()
        passengerModel.ViewUserPassengers(str(item).split()[1])
        passengerLoad = passengerModel.UserPassenger
        self.userPassengersID = {}
        if passengerLoad is not None:
            for passenger in passengerLoad:
                itemText = str(passenger[1]) + ' ' + str(passenger[2])
                item = QtWidgets.QListWidgetItemitemText
                self.CustomerUi.lstPassengers.addItem(item)
                self.userPassengersID[itemText] = passenger[0]               
    def ListUserPassengersClicked(self, item):
        passengerModel = Passengers()
        passengerModel.FindPassenger(self.userPassengersID[item.text()])
        passenger = passengerModel.FlightPassenger
        self.CustomerUi.lblFName.setText(passenger[1])
        self.CustomerUi.lblLName.setText(passenger[2])
        self.CustomerUi.lblGender.setText(passenger[3])
        self.CustomerUi.lblAge.setText(passenger[4])
    def ChangePasswordClicked(self):
        try:
            userModel = Users()
            userModel.ViewUser(self.UserID)
            password = userModel.User[5]
            currentPass = self.CustomerUi.txtCurrentPassword.text()
            newPass = self.CustomerUi.txtNewPassword.text()
            confirmPass = self.CustomerUi.txtConfirmPassword.text()
            
            if (currentPass != password) or (newPass != confirmPass):
                raise Exception('Incorrect Password!')
            userModel.UpdateUserPassword(self.UserID, newPass)
            self.MessageBox('Password successfully changed!', True)
        except Exception as e:
            self.MessageBox(str(e), False)


        

    
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
