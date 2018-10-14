from dbHelper import dbHelper

db = dbHelper("db_FlightReservation.db")

countries = []
countries.append('Philippines')
countries.append('United States')
countries.append('Japan')
countries.append('Indonesia')
countries.append('Argentina')
countries.append('Poland')
countries.append('Belgium')
countries.append('Chile')
countries.append('Saudi Arabia')

cities = []
cities.append('Manila')
cities.append('New York City')
cities.append('Tokyo')
cities.append('Bali')
cities.append('Buenos Aires')
cities.append('Bydgoszcz')
cities.append('Brussels')
cities.append('Santiago de Chile')
cities.append('Riyadha')

i = 0
cmd = "DELETE FROM COUNTRY "
cmd += "DELETE FROM CITY "
cmd += "DELETE FROM LOCATION"
db.ExecuteCommand(cmd)
for x in countries:
    cmd = "INSERT INTO COUNTRY(COUNTRYNAME) VALUES('" + x + "') "
    db.ExecuteCommand(cmd)
    cmd = "INSERT INTO CITY(CITYNAME) VALUES('" + cities[i] + "') "
    db.ExecuteCommand(cmd)
    cmd = "SELECT * FROM COUNTRY WHERE COUNTRYNAME = '" + x + "' "
    db.ExecuteCommand(cmd)
    countryID = db.Data[0]
    cmd = "SELECT * FROM CITY WHERE CITYNAME = '" + cities[i] + "' "
    db.ExecuteCommand(cmd)
    cityID = db.Data[0]
    cmd = "INSERT INTO LOCATION(COUNTRYID, CITYID) VALUES(" + str(countryID) + ", " + str(cityID) + ") "
    db.ExecuteCommand(cmd)
    i += 1