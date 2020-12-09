import mysql.connector

cnx = mysql.connector.connect(user='joseph', password='passcode',
                              host='localhost',
                              database='SmartGreenhouse')
cnx.close()
