# -*- coding: utf-8 -*-
#Models.py
#Classes that access database

from Database.dbHelper import dbHelper

class Models:
    __hasError = None
    __errorMessage = None
    dataSource = 'Database/db_FlightReservation.db' 

    @property
    def HasError(self):
        return self.__hasError
    
    @HasError.setter
    def HasError(self, hasError):
        self.__hasError = hasError
    
    @property
    def ErrorMessage(self):
        return self.__errorMessage
    
    @ErrorMessage.setter
    def ErrorMessage(self, errorMessage):
        self.__errorMessage = errorMessage

#Users Class
class Users(Models):
    user = None
    allUser = None

    @property
    def User(self):
        return self.user
    @property
    def AllUser(self):
        return self.allUser
    def FindUser(self, username, password = None):
        try:
            db = dbHelper(self.dataSource)
            if password is not None:
                db.ExecuteCommand("SELECT * FROM User WHERE USERNAME = '" + username + "' AND PASSWORD = '" + password + "'")
            else:
                db.ExecuteCommand("SELECT * FROM User WHERE USERNAME = '" + username + "'")

            self.user = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)  
    def ViewAllUser(self):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM USER")
            self.allUser = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def AddUser(self, userInfo):
        try:
            sqlCommand = '''
                INSERT INTO User(FNAME, LNAME, EMAIL, USERNAME, PASSWORD, ADDRESS, DATEBIRTH, GENDER, CONTACTNUM) 
                VALUES(?,?,?,?,?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, userInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)     
    def DeleteUser(self, userID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("DELETE User WHERE UserID = " + userID)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)

#Flights Class
class Flights(Models):
    flight = None
    allFlight = None

    @property
    def Flight(self):
        return self.flight
    @property
    def AllFlight(self):
        return self.allFlight
    def ViewAllFlights(self):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("Select * From Flight")
            self.allFlight = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def AddFlight(self, flightInfo):
        try:
            sqlCommand = '''
                INSERT INTO Flight(ORIGINID, DESTINATIONID, PRICE, SEATS, DEPARTUREDATE, ARRIVALDATE, DEPARTURETIME, ARRIVALTIME, REMARKS) 
                VALUES(?,?,?,?,?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, flightInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e) 
    def DeleteFlight(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("DELETE Flight WHERE FlightID = " + flightID)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def UpdateFlight(self, flightID, remarks):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("UPDATE Flight SET REMARKS = '" + remarks + "' WHERE Flight = " + flightID)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
            
#Passengers Class
class Passengers(Models):
    userPassenger = None
    flightPassengers = None
    availSeats = 0
    __seats = None
    __taken = None

    @property
    def UserPassenger(self):
        return self.userPassenger  
    @property
    def FlightPassengers(self):
        return self.flightPassengers
    @property
    def AvailSeats(self):
        if self.availSeats is None:
            return 0
        return self.availSeats
    def ViewFlightPassenger(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE FLIGHTID = " + flightID)
            self.flightPassengers = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def DeleteFlightPassengers(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("DELETE PASSENGER WHERE FlightID = " + flightID)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewUserPassengers(self, userID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE USERID = " + userID)
            self.userPassenger = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def AddUserPassengers(self, passengerInfo):
        try:
            sqlCommand = '''
                INSERT INTO Flight(FNAME, LNAME, GENDER, AGE, FLIGHTID, USERID) 
                VALUES(?,?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, passengerInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e) 
    def ViewAvailableSeats(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT SEATS FROM FLIGHT WHERE Flight = " + flightID)
            self.__seats = db.Data
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE Flight = " + flightID)
            self.__taken = len(db.DataTable)
            
            self.availSeats = self.__seats - self.__taken

            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)

#Payments Class
class Payments(Models):
    payments = None
    userPayment = None

    @property
    def Payments(self):
        return self.payments
    @property
    def UserPayment(self):
        return self.userPayment 
    def ViewPayments(self):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PAYMENT")
            self.payments = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewUserPayment(self, userID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PAYMENT WHERE USERID = " + userID)
            self.userPayment = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def AddPayment(self, paymentInfo):
        try:
            sqlCommand = '''
                INSERT INTO Flight(USERID, CARDNUMBER, CARD, EXPIRYDATE, CSC) 
                VALUES(?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, paymentInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e) 


    
        


        
        