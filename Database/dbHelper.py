import sqlite3

class dbHelper:
    __dataSource = None
    __sqlConnection = None
    __sqlCursor = None
    __result = None
    __data = None
    __dataTable = None
    __hasError = False
    __error = None

    def __init__(self, db_File):
        self.__dataSource = db_File
        self. __hasError = False

    @property
    def Data(self):
        return self.__data

    @property
    def DataTable(self):
        return self.__dataTable
       
    @property
    def HasError(self):
        return self.__hasError
   
    @property
    def ErrorMessage(self):
        return "An error has occurred: " + self.__error

    def ConnectionOpen(self):
       self. __sqlConnection = sqlite3.connect(self.__dataSource)

    def ConnectionClose(self):
        self.__sqlConnection.commit()
        self.__sqlConnection.close()

    def ExecuteCommand(self, sqlCommand = None, sqlValues = None):
        try:
            self.ConnectionOpen()
            self.__sqlCursor = self.__sqlConnection.cursor()
            if sqlValues is not None:
                self.__result = self.__sqlConnection.execute(sqlCommand, sqlValues)
            else:
                self.__result = self.__sqlConnection.execute(sqlCommand)
            self.__dataTable = self.__result.fetchall()
            self.__data = self.__dataTable[0]
            self.ConnectionClose()
            self.__hasError = False
        except Exception as e:
           self. __hasError = True
           self.__error = str(e)
           print(self.ErrorMessage())

    

        



