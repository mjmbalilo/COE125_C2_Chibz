# -*- coding: utf-8 -*-

import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from Views.Signup import Ui_SignupWindow
from Views.Admin import Ui_AdminWindow
from Views.Customer import Ui_CustomerWindow
from Views.Login import Ui_LoginWindow
from Views.Passenger import Ui_PassengerWindow
from Views.Payment import Ui_PaymentWindow
from Models import Users, Flights, Passengers, Payments, Locations, Admin

class Ui_Controllers:
    UserID = None
    AdminID = None
    FlightID = None
    MyFlightID = None
    FlightInfo = []
    IsTimeClicked = False

    #region UI
    def Login(self):
        self.LoginWindow = QtWidgets.QDialog()
        self.LoginUi = Ui_LoginWindow()
        self.LoginUi.setupUi(self.LoginWindow)
        self.SetupLoginEvents()
        self.LoginWindow.show()
    def Customer(self):
        self.LoginWindow.hide() 
        self.CustomerWindow = QtWidgets.QDialog()
        self.CustomerUi = Ui_CustomerWindow()
        self.CustomerUi.setupUi(self.CustomerWindow)
        self.SetupCustomerEvents()
        self.CustomerWindow.show()
    def Passenger(self):
        self.PassengerWindow = QtWidgets.QDialog()
        self.PassengerUi = Ui_PassengerWindow()
        self.PassengerUi.setupUi(self.PassengerWindow, self.PassengerNum)
        self.SetupPassengerEvents()
        self.PassengerWindow.show()
    def Payment(self):
        self.PaymentWindow = QtWidgets.QDialog()
        self.PaymentUi = Ui_PaymentWindow()
        self.PaymentUi.setupUi(self.PaymentWindow)
        self.SetupPaymentEvents()
        self.PaymentWindow.show() 
    def Signup(self):
        self.LoginWindow.hide() 
        self.SignUpWindow = QtWidgets.QDialog()
        self.SignupUi = Ui_SignupWindow()
        self.SignupUi.setupUi(self.SignUpWindow)
        self.SetupSignUpEvents()
        self.SignUpWindow.show()
    def Admin(self):
        self.LoginWindow.hide() 
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
            self.AdminID = loginCtr.AdminID

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
        self.DisplayCurrentDate()
        self.DisplayFlights()
        self.DisplayUsers()
        self.DisplayFlightCountries()
        self.AdminUi.btnDeleteFlight.clicked.connect(self.DeleteFlightClicked)
        self.AdminUi.btnUpdateFlight.clicked.connect(self.UpdateFlightClicked)
        self.AdminUi.btnAddFlight.clicked.connect(self.AddFlightClicked)
        self.AdminUi.cbxOriginCountry.activated.connect(self.CbxFlightOriginCountryClicked)
        self.AdminUi.cbxDestinationCountry.activated.connect(self.CbxFlightDestinationCountryClicked)
        self.AdminUi.cbxFlightPassengers.activated.connect(self.CbxFlightPassengersClicked)
        self.AdminUi.lstFlights.currentItemChanged.connect(self.ListFlightsClickied)
        self.AdminUi.lstPassengers.currentItemChanged.connect(self.ListPassengersClicked)
        self.AdminUi.lstUsers.currentItemChanged.connect(self.ListUsersClicked)
        self.AdminUi.btnDeleteUser.clicked.connect(self.DeleteUserClicked)
        self.AdminUi.btnChangeUsername.clicked.connect(self.ChangeAdminUsernameClicked)
        self.AdminUi.btnChangePassword.clicked.connect(self.ChangeAdminPasswordClicked)
    def DisplayCurrentDate(self):
        now = datetime.datetime.now()
        self.AdminUi.txtTravelDate.setDateTime(QtCore.QDateTime(QtCore.QDate(now.year, now.month, now.day), QtCore.QTime(0, 0, 0)))
    def DisplayFlights(self):
        flightModel = Flights()
        flightModel.ViewAllFlights()
        flightLoad = flightModel.AllFlight
        self.AdminUi.lstFlights.clear()
        self.AdminUi.cbxFlightPassengers.clear()
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
    def DisplayFlightCountries(self):
        locationModel = Locations()
        locationModel.ViewAllCountry()
        countryLoad = locationModel.Country
        if countryLoad is not None:
            for country in countryLoad:
                self.AdminUi.cbxOriginCountry.addItem(str(country[0]))
                self.AdminUi.cbxDestinationCountry.addItem(str(country[0]))
    
    def ClearFlightDetails(self):
        self.AdminUi.lblOrigin.setText('')
        self.AdminUi.lblDestination.setText('')
        self.AdminUi.lblPrice.setText('')
        self.AdminUi.lblTravelDate.setText('')
        self.AdminUi.lblTravelTime.setText('')
        self.AdminUi.txtRemarks.setText('')
        self.AdminUi.lblAvailSeats.setText('')
    def ListFlightsClickied(self, item):
        try:
            flightModel = Flights()
            locationModel = Locations()
            passengerModel = Passengers()
            flightModel.FindFlight(str(item.text()).split()[1])
            flight = flightModel.Flight
            locationModel.ViewLocation(flight[1])
            origin = locationModel.Location[0] + ', ' + locationModel.Location[1]
            locationModel.ViewLocation(flight[2])
            destination = locationModel.Location[0] + ', ' + locationModel.Location[1]
            passengerModel.ViewAvailableSeats(flight[0])
            availSeats = passengerModel.AvailSeats
            self.FlightID = flight[0]
            self.AdminUi.lblOrigin.setText(origin)
            self.AdminUi.lblDestination.setText(destination)
            self.AdminUi.lblPrice.setText(str(flight[3]))
            self.AdminUi.lblTravelDate.setText(flight[4])
            self.AdminUi.lblTravelTime.setText(flight[5])
            self.AdminUi.txtRemarks.setText(flight[6])
            self.AdminUi.lblAvailSeats.setText(str(availSeats))

        except Exception as e:
            self.MessageBox(str(e), False)
    def DeleteFlightClicked(self):
        try:
            if(self.FlightID is None):
                raise Exception("Select Flight First!")
            flightModel = Flights()
            flightModel.DeleteFlight(self.FlightID)
            if(flightModel.HasError):
                raise Exception(flightModel.ErrorMessage)
            self.MessageBox('Flight successfully deleted!', True)
            self.DisplayFlights()
            self.ClearFlightDetails()
        except Exception as e:
            self.MessageBox(str(e), False)       
    def UpdateFlightClicked(self):
        try:
            if(self.FlightID is None):
                raise Exception("Select Flight First!")
            flightModel = Flights()
            remarks = self.AdminUi.txtRemarks.text()
            flightModel.UpdateFlight(self.FlightID, remarks)
            self.MessageBox('Flight successfully updated!', True)
        except Exception as e:
            self.MessageBox(str(e), False)  
    def AddFlightClicked(self):
        try:
            flightInfo = []
            flightModel = Flights()
            locationModel = Locations()
            originCity = self.AdminUi.cbxOriginCity.currentText()
            destinationCity = self.AdminUi.cbxDestinationCity.currentText()
            if originCity is '' or destinationCity is '':
                raise Exception('Invalid Origin and Destination')
            locationModel.ViewLocationID(self.AdminUi.cbxOriginCountry.currentText(), originCity)
            originID = locationModel.LocationID[0]
            locationModel.ViewLocationID(self.AdminUi.cbxDestinationCountry.currentText(), destinationCity)
            destinationID = locationModel.LocationID[0]
            flightInfo.append(originID)
            flightInfo.append(destinationID)
            flightInfo.append(self.AdminUi.txtPrice.text())
            flightInfo.append(self.AdminUi.txtTravelDate.text())
            flightInfo.append(self.AdminUi.txtTravelTime.text())
            flightInfo.append('Available')
            flightInfo.append(self.AdminUi.txtSeats.text())
            for info in flightInfo:
                if info is '':
                    raise Exception('Please fill up the required fields!')
            if(originID == destinationID):
                raise Exception('Invalid Origin and Destination')
            currentDate = datetime.datetime.now().strftime("%m/%d/%Y")
            inputDate = flightInfo[2]
            if(inputDate < currentDate):
                raise Exception('Invalid Travel Date')
            flightModel.AddFlight(flightInfo)
            if(flightModel.HasError):
                raise Exception(flightModel.ErrorMessage)
            self.MessageBox('Flight successfully added!', True)
            self.DisplayFlights()
        except Exception as e:
            self.MessageBox(str(e), False)

    def CbxFlightOriginCountryClicked(self):
        locationModel = Locations()
        country = self.AdminUi.cbxOriginCountry.currentText()
        locationModel.ViewCountryCities(country)
        cityLoad = locationModel.City
        self.AdminUi.cbxOriginCity.clear()
        if cityLoad is not None:
            for city in cityLoad:
                self.AdminUi.cbxOriginCity.addItem(str(city[0]))
    def CbxFlightDestinationCountryClicked(self):
        locationModel = Locations()
        country = self.AdminUi.cbxDestinationCountry.currentText()
        locationModel.ViewCountryCities(country)
        cityLoad = locationModel.City
        self.AdminUi.cbxDestinationCity.clear()
        if cityLoad is not None:
            for city in cityLoad:
                self.AdminUi.cbxDestinationCity.addItem(str(city[0]))
    def CbxFlightPassengersClicked(self):
        try:
            passengerModel = Passengers()
            item = self.AdminUi.cbxFlightPassengers.currentText()
            passengerModel.ViewAllFlightPassengers(str(item).split()[1])
            passengerLoad = passengerModel.AllFlightPassengers
            self.flightPassengerID = {}
            if passengerLoad is not None:
                for passenger in passengerLoad:
                    itemText = str(passenger[1]) + ' ' + str(passenger[2])
                    self.AdminUi.lstPassengers.addItem(itemText)
                    self.flightPassengerID[itemText] = passenger[0]
        except Exception as e:
            self.MessageBox(str(e), False)
        
    def ListPassengersClicked(self, item):
        try:
            passengerModel = Passengers()
            passengerModel.FindPassenger(self.flightPassengerID[item.text()])
            passenger = passengerModel.FlightPassenger
            self.AdminUi.lblFName.setText(passenger[1])
            self.AdminUi.lblLName.setText(passenger[2])
            self.AdminUi.lblGender.setText(passenger[3])
            self.AdminUi.lblAge.setText(passenger[4])
        except Exception as e:
            self.MessageBox(str(e), False) 
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
    def ChangeAdminUsernameClicked(self):
        try:
            adminModel = Admin()
            adminModel.FindAdmin(None, None, self.AdminID)
            print(str(self.AdminID))
            username = adminModel.Admin[1]
            currentUsername = self.AdminUi.txtCurrentUsername.text()
            newUsername = self.AdminUi.txtNewUsername.text()
            
            if (currentUsername != username):
                raise Exception('Incorrect Username!')
            adminModel.UpdateAdminUsername(self.AdminID, newUsername)
            self.MessageBox('Username successfully changed!', True)
        except Exception as e:
            self.MessageBox(str(e), False)
    def ChangeAdminPasswordClicked(self):
        try:
            adminModel = Admin()
            adminModel.FindAdmin(None, None, self.AdminID)
            password = adminModel.Admin[2]
            currentPass = self.AdminUi.txtCurrentPassword.text()
            newPass = self.AdminUi.txtNewPassword.text()
            confirmPass = self.AdminUi.txtConfirmPassword.text()
            
            if (currentPass != password) or (newPass != confirmPass):
                raise Exception('Incorrect Password!')
            adminModel.UpdateAdminPassword(self.AdminID, newPass)
            self.MessageBox('Password successfully changed!', True)
        except Exception as e:
            self.MessageBox(str(e), False)
    #endregion

    #region Customer
    def SetupCustomerEvents(self):
        self.DisplayCountry()
        self.DisplayUserAccount()
        self.CustomerUi.tabWidget.currentChanged.connect(self.DisplayMyFlights)
        self.CustomerUi.cbxOriginCountry.activated.connect(self.CbxOriginCountryClicked)
        self.CustomerUi.cbxDestinationCountry.activated.connect(self.CbxDestinationCountryClicked)
        self.CustomerUi.btnBookFlight.clicked.connect(self.BookFlightClicked)
        self.CustomerUi.btnChangePassword.clicked.connect(self.ChangePasswordClicked)
        self.CustomerUi.cbxFlights.activated.connect(self.CbxUserFlightsClicked)
        self.CustomerUi.lstPassengers.currentItemChanged.connect(self.ListUserPassengersClicked)
        self.CustomerUi.btnLogout.clicked.connect(self.LogoutClicked)
    def DisplayCountry(self):
        locationModel = Locations()
        locationModel.ViewAllCountry()
        countryLoad = locationModel.Country
        if countryLoad is not None:
            for country in countryLoad:
                self.CustomerUi.cbxOriginCountry.addItem(str(country[0]))
                self.CustomerUi.cbxDestinationCountry.addItem(str(country[0]))
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
        try:
            flightModel = Flights()
            locationModel = Locations()
            originCountry = self.CustomerUi.cbxOriginCountry.currentText()
            destinationCountry = self.CustomerUi.cbxDestinationCountry.currentText()
            originCity = self.CustomerUi.cbxOriginCity.currentText()
            destinationCity = self.CustomerUi.cbxDestinationCity.currentText()
            if originCity is '' or destinationCity is '':
                raise Exception('Invalid Origin and Destination')

            locationModel.ViewLocationID(originCountry, originCity)
            originID = locationModel.LocationID[0]
            locationModel.ViewLocationID(destinationCountry, destinationCity)
            destinationID = locationModel.LocationID[0]

            travelDate = self.CustomerUi.txtDate.text()
            self.FlightInfoID = [originID, destinationID, travelDate]
            self.FlightInfo = []
            self.FlightInfo.append(originCity + ', ' + originCountry)
            self.FlightInfo.append(destinationCity + ', ' + destinationCountry)
            self.FlightInfo.append(travelDate)
            flightModel.FindFlight(None, self.FlightInfoID)
            self.Flights = flightModel.Flight
            if(self.Flights == []):
                raise Exception('Invalid Flight')
            self.PassengerNum = {}
            self.PassengerNum["Adult"] = self.CustomerUi.txtAdult.text()
            self.PassengerNum["Infant"] = self.CustomerUi.txtInfant.text()
            self.PassengerNum["Child"] = self.CustomerUi.txtChildren.text()
            self.PassengerNum["Senior Citizen"] = self.CustomerUi.txtSeniorCitizen.text()
            if(int(self.PassengerNum["Adult"]) <= 0):
                raise Exception('Please add passengers...')
            self.Passenger()
        except Exception as e:
            self.MessageBox(str(e), False)
    def CbxUserFlightsClicked(self):
        try:
            flightModel = Flights()
            locationModel = Locations()
            passengerModel = Passengers()
            item = self.CustomerUi.cbxFlights.currentText()

            flightModel.FindFlight(str(item).split()[1])
            flightInfo = flightModel.Flight
            locationModel.ViewLocation(flightInfo[1])
            originCountry = locationModel.Location[0]
            originCity = locationModel.Location[1]
            locationModel.ViewLocation(flightInfo[2])
            destinationCountry = locationModel.Location[0]
            destinationCity = locationModel.Location[1]
            passengerModel.ViewAvailableSeats(flightInfo[0])
            availSeats = passengerModel.AvailSeats

            self.CustomerUi.lblOrigin.setText(originCity + ', ' + originCountry)
            self.CustomerUi.lblDestination.setText(destinationCity + ', ' + destinationCountry)
            self.CustomerUi.lblTravelDate.setText(str(flightInfo[4]))
            self.CustomerUi.lblTravelTime.setText(str(flightInfo[5]))
            self.CustomerUi.lblPrice.setText(str(flightInfo[3]))
            self.CustomerUi.lblAvailSeats.setText(str(availSeats))
            self.CustomerUi.lblRemarks.setText(str(flightInfo[6]))

            passengerModel.ViewUserPassengers(self.UserID, str(item).split()[1])
            if(passengerModel.HasError):
                raise Exception(passengerModel.ErrorMessage)
            passengerLoad = passengerModel.UserPassenger
            self.userPassengersID = {}
            if passengerLoad is not []:
                for passenger in passengerLoad:
                    itemText = str(passenger[1]) + ' ' + str(passenger[2])
                    self.CustomerUi.lstPassengers.addItem(itemText)
                    self.userPassengersID[itemText] = passenger[0]
        except Exception as e:
            self.MessageBox(str(e), False)                       
    def ListUserPassengersClicked(self, item):
        try:
            passengerModel = Passengers()
            passengerModel.FindPassenger(self.userPassengersID[item.text()])
            passenger = passengerModel.FlightPassenger
            self.CustomerUi.lblFName.setText(passenger[1])
            self.CustomerUi.lblLName.setText(passenger[2])
            self.CustomerUi.lblGender.setText(passenger[3])
            self.CustomerUi.lblAge.setText(passenger[4])
        except Exception as e:
            self.MessageBox(str(e), False)         
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
    def LogoutClicked(self):
        self.CustomerWindow.close()
        self.Login()
    #endregion

    #region Passenger
    def SetupPassengerEvents(self):
        self.PassengerUi.btnAddPassenger.clicked.connect(self.AddPassengerClicked)
    def AddPassengerClicked(self):
        try:
            self.PassengerInfo = self.PassengerUi.PassengerInfo
            self.Payment()
        except Exception as e:
            self.MessageBox(str(e), False)
    #endregion

    #region Payment
    def SetupPaymentEvents(self):
        self.DisplayPaymentDetails()
        self.PaymentUi.btnConfirmFlight.clicked.connect(self.ConfirmFlightClicked)
        self.PaymentUi.cbxTime.activated.connect(self.TimeClicked)
    def DisplayPaymentDetails(self):
        try: 
            for flight in self.Flights:
                self.PaymentUi.cbxTime.addItem(str(flight[5]))

            self.PaymentUi.lblOrigin.setText(str(self.FlightInfo[0]))
            self.PaymentUi.lblDestination.setText(str(self.FlightInfo[1]))
            self.PaymentUi.lblTravelDate.setText(str(self.FlightInfo[2]))
            passengerTxt = ''
            for passenger in self.PassengerNum:
                if(int(self.PassengerNum[passenger]) > 0):
                    passengerTxt += "%s(%s), " %(str(self.PassengerNum[passenger]), str(passenger)[0])
            
            self.PaymentUi.lblPassengers.setText(str(passengerTxt))
        except Exception as e:
            self.MessageBox(str(e), False)
    def TimeClicked(self):
        try: 
            flightModel = Flights()
            time = self.PaymentUi.cbxTime.currentText()
            flightModel.FindFlight(None, self.FlightInfoID, time)
            self.FlightID = flightModel.Flight[0]
            price = flightModel.Flight[3]
            totalPrice = 0
            for passenger in self.PassengerNum:
                multiplier = float(self.PassengerNum[passenger])
                if(passenger == "Adult"):
                    totalPrice += (multiplier * price)
                elif(passenger == "Infant"):
                    totalPrice += (multiplier * price) * 0.05
                elif(passenger == "Child"):
                    totalPrice += (multiplier * price) * .80
                elif(passenger == "Senior Citizen"):
                    totalPrice += (multiplier * price) * .80
            self.PaymentUi.lblPrice.setText(str(price))
            self.PaymentUi.lblTotalPrice.setText(str(totalPrice))
            self.IsTimeClicked = True
        except Exception as e:
            self.MessageBox(str(e), False)
    def ConfirmFlightClicked(self):
        try:   
            passengerModel = Passengers()
            paymentModel = Payments()
            if not self.IsTimeClicked:
                raise Exception('Choose Time!')
            paymentInfo = []
            paymentInfo.append(self.UserID)
            paymentInfo.append(self.PaymentUi.txtCardNum.text())
            paymentInfo.append(self.PaymentUi.cbxCard.currentText())
            paymentInfo.append(self.PaymentUi.txtExpDate.text())
            paymentInfo.append(self.PaymentUi.txtCSC.text())
            paymentInfo.append(self.PaymentUi.lblTotalPrice.text())
            paymentInfo.append(self.FlightID)
            for info in paymentInfo:
                if info == '':
                    raise Exception('Please input card details.')
            paymentModel.AddPayment(paymentInfo)
            if(paymentModel.HasError):
                raise Exception(paymentModel.ErrorMessage)
            for age in self.PassengerInfo:
                for txt in self.PassengerInfo[age]:
                    passInfo = [txt[0], txt[1], txt[2], age, self.FlightID, self.UserID]
                    passengerModel.AddUserPassengers(passInfo)
                    if(passengerModel.HasError):
                        raise Exception(passengerModel.ErrorMessage)
            self.MessageBox('Flight Booked!', True)
            self.PaymentWindow.close()
            self.PassengerWindow.close()
        except Exception as e:
            self.MessageBox(str(e), False)
    #endregion

class Controllers:
    __window = None
    __userID = None
    __adminID = None
    __hasError = False
    __errorMessage = None

    @property
    def Window(self):
        return self.__window
    @property
    def UserID(self):
        return self.__userID
    @property
    def AdminID(self):
        return self.__adminID
    @property
    def HasError(self):
        return self.__hasError
    @property
    def ErrorMessage(self):
        return self.__errorMessage

    def LoginCheck(self, username, password):        
        try:
            if not (username and password):
                raise Exception('Please fill up the required fields!')

            userModel = Users()
            adminModel = Admin()
            userModel.FindUser(username, password)
            adminModel.FindAdmin(username, password)
            user = userModel.User
            admin = adminModel.Admin 
            if user is not None:
                userID = user[0]
                self.__window = "CUSTOMER"
                self.__userID = userID
                self.__hasError = False        
            elif admin is not None:
                adminID = admin[0]
                self.__window = "ADMIN"
                self.__adminID = adminID
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
