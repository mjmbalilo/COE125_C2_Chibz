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

#Admin Class(Models):
class Admin(Models):
    admin = None

    @property
    def Admin(self):
        return self.admin
    def FindAdmin(self, username = None, password = None, adminID = None):
        try:
            db = dbHelper(self.dataSource)
            if adminID is not None:
                db.ExecuteCommand("SELECT * FROM Admin WHERE AdminID = " + str(adminID))
            else:
                db.ExecuteCommand("SELECT * FROM Admin WHERE USERNAME = '" + username + "' AND PASSWORD = '" + password + "'")
            self.admin = db.Data
            db.ExecuteCommand("SELECT * FROM User WHERE USERNAME = '%s'" %username)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def UpdateAdminUsername(self, adminID = None, username = None):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("UPDATE Admin SET Username = '%s' WHERE AdminID = %s;" %(username, str(adminID)))
            db.ExecuteCommand("SELECT * FROM User WHERE USERNAME = '%s'" %username)
            if db.Data != ():
                raise Exception('Invalid username!')
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def UpdateAdminPassword(self, adminID = None, password = None):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("UPDATE Admin SET Password = '%s' WHERE AdminID = %s;" %(password, str(adminID)))
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)

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
    def FindUser(self, username = None, password = None, userID = None):
        try:
            db = dbHelper(self.dataSource)
            if userID is not None:
                db.ExecuteCommand("SELECT * FROM User WHERE UserID = " + str(userID))
            elif password is not None:
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
            db.ExecuteCommand("SELECT * FROM Admin WHERE USERNAME = '%s'" %userInfo[3])
            if db.Data != ():
                raise Exception('Invalid username!')
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)     
    def DeleteUser(self, userID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("DELETE FROM USER WHERE UserID = " + str(userID))
            db.ExecuteCommand("DELETE FROM PASSENGER WHERE UserID = " + str(userID))
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def UpdateUserPassword(self, userID, password):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("UPDATE User SET PASSWORD = '" + password + "' WHERE UserID = " + str(userID))
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewUser(self, userID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM User WHERE UserID = " + str(userID))
            self.user = db.Data
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
    def FindFlight(self, flightID = None, flightInfo = None, time = None):
        try:
            db = dbHelper(self.dataSource)
            if(flightID is not None):
                db.ExecuteCommand("Select * From Flight Where FlightID = " + flightID)
                self.flight = db.Data
            elif(flightInfo is not None and time is None):
                cmd = '''SELECT * FROM FLIGHT
                        WHERE FLIGHT.ORIGINID = %s
                        AND FLIGHT.DESTINATIONID = %s
                        AND TRAVELDATE = '%s';''' % (str(flightInfo[0]), str(flightInfo[1]), str(flightInfo[2]))
                db.ExecuteCommand(cmd)
                self.flight = db.DataTable
            elif(time is not None):
                cmd = '''SELECT * FROM FLIGHT
                        WHERE FLIGHT.ORIGINID = %s
                        AND FLIGHT.DESTINATIONID = %s
                        AND TRAVELDATE = '%s'
                        AND TRAVELTIME = '%s';''' % (str(flightInfo[0]), str(flightInfo[1]), str(flightInfo[2]), str(time))
                db.ExecuteCommand(cmd)
                self.flight = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
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
                INSERT INTO Flight(ORIGINID, DESTINATIONID, PRICE, TRAVELDATE, TRAVELTIME, REMARKS, SEATS) 
                VALUES(?,?,?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, flightInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
            print('Add Flight Error: ' + str(e))
    def DeleteFlight(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("DELETE FROM PASSENGER WHERE FlightID = " + str(flightID))
            db.ExecuteCommand("DELETE FROM FLIGHT WHERE FlightID = " + str(flightID))
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def UpdateFlight(self, flightID, remarks):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("UPDATE Flight SET REMARKS = '" + remarks + "' WHERE FlightID = " + str(flightID))
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
            print('Update Flight Error: ' + str(e))

#Location Class
class Locations(Models):
    location = None
    locationID = None
    country = None
    city = None

    @property
    def Country(self):
        return self.country
    @property
    def City(self):
        return self.city
    @property
    def Location(self):
        return self.location
    @property
    def LocationID(self):
        return self.locationID
    def ViewLocation(self, locationID):
        try:
            db = dbHelper(self.dataSource)
            cmd = '''SELECT COUNTRY.COUNTRYNAME, CITY.CITYNAME FROM CITY 
                        INNER JOIN LOCATION ON CITY.CITYID = LOCATION.CITYID 
                        INNER JOIN COUNTRY ON COUNTRY.COUNTRYID = LOCATION.COUNTRYID 
                        WHERE LOCATION.LOCATIONID = '%s';''' %locationID
            db.ExecuteCommand(cmd)
            self.location = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewLocationID(self, country, city):
        try:
            db = dbHelper(self.dataSource)
            cmd = '''SELECT LOCATION.LOCATIONID FROM CITY 
                        INNER JOIN LOCATION ON CITY.CITYID = LOCATION.CITYID 
                        INNER JOIN COUNTRY ON COUNTRY.COUNTRYID = LOCATION.COUNTRYID 
                        WHERE COUNTRY.COUNTRYNAME = '%s' 
                        AND CITY.CITYNAME = '%s';''' % (country, city)
            db.ExecuteCommand(cmd)
            self.locationID = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewAllCountry(self):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT COUNTRY.COUNTRYNAME FROM COUNTRY")
            self.country = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewCountryCities(self, country):
        try:
            db = dbHelper(self.dataSource)
            cmd = '''SELECT CITY.CITYNAME FROM CITY 
                        INNER JOIN LOCATION ON CITY.CITYID = LOCATION.CITYID 
                        INNER JOIN COUNTRY ON COUNTRY.COUNTRYID = LOCATION.COUNTRYID 
                        WHERE COUNTRY.COUNTRYNAME = '%s';''' %country
            db.ExecuteCommand(cmd)
            self.city = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)

#Passengers Class
class Passengers(Models):
    userFlights = None
    userPassenger = None
    flightPassenger = None
    allFlightPassengers = None
    availSeats = 0
    __seats = None
    __taken = None

    @property
    def UserFlights(self):
        return self.userFlights  
    @property
    def UserPassenger(self):
        return self.userPassenger  
    @property
    def FlightPassenger(self):
        return self.flightPassenger  
    @property
    def AllFlightPassengers(self):
        return self.allFlightPassengers
    @property
    def AvailSeats(self):
        if self.availSeats is None:
            return 0
        return self.availSeats
    def ViewUserFlights(self, userID):
        try:
            db = dbHelper(self.dataSource)
            cmd = '''SELECT FLIGHT.FLIGHTID FROM FLIGHT 
                        INNER JOIN PASSENGER ON FLIGHT.FLIGHTID = PASSENGER.FLIGHTID 
                        WHERE PASSENGER.PASSENGERID = %s;''' %userID
            db.ExecuteCommand(cmd)
            self.userFlights = db.DataTable
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def FindPassenger(self, passengerID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE PASSENGERID = " + str(passengerID))
            self.flightPassenger = db.Data
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
    def ViewAllFlightPassengers(self, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE FLIGHTID = " + flightID)
            self.allFlightPassengers = db.DataTable
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
    def ViewUserPassengers(self, userID, flightID):
        try:
            db = dbHelper(self.dataSource)
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE USERID = %s AND FLIGHTID = %s" %(str(userID), str(flightID)))
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
                INSERT INTO PASSENGER(FNAME, LNAME, GENDER, AGE, FLIGHTID, USERID) 
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
            db.ExecuteCommand("SELECT SEATS FROM FLIGHT WHERE FlightID = " + str(flightID))
            self.__seats = db.Data[0]
            db.ExecuteCommand("SELECT * FROM PASSENGER WHERE FlightID = " + str(flightID))
            self.__taken = len(db.DataTable)
            self.availSeats = int(self.__seats) - int(self.__taken)

            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e)
            print(self.ErrorMessage)

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
                INSERT INTO PAYMENT(USERID, CARDNUMBER, CARD, EXPIRYDATE, CSC, TOTALPRICE, FLIGHTID) 
                VALUES(?,?,?,?,?,?,?)'''
            db = dbHelper(self.dataSource)
            db.ExecuteCommand(sqlCommand, paymentInfo)
            if(db.HasError):
                raise Exception(db.ErrorMessage)
            self.HasError = False
        except Exception as e:
            self.HasError = True
            self.ErrorMessage = str(e) 


    
        


        
        
