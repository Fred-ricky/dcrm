import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ricky1209'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All Done!")