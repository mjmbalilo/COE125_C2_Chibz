from Database.dbHelper import dbHelper

db = dbHelper('Database/db_FlightReservation.db')
db.ExecuteCommand("SELECT * FROM USER")
print(db.Data)
print(db.DataTable)

