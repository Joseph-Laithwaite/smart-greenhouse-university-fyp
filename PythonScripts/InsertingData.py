import mysql.connector
from mysql.connector import errorcode


config={
    'user':'joseph',
    'password':'passcode',
    'host':'localhost',
    'database':'SmartGreenhouse',
    'raise_on_warnings':True,
}

#try:
cnx = mysql.connector.connect(**config)
#except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#  cnx.close()

#try:
cursor = cnx.cursor()
#except:
#    print("Cursor not formed")

add_farmer = ("INSERT INTO SmartGreenhouse.Farmer"
              "(FarmerID,FarmerEmail,FarmerName,FarmerPassword)"
              "VALUES (%(FarmerID)s,%(FarmerEmail)s,%(FarmerName)s,PASSWORD(\"%(FarmerPassword)s\"));"
              )




data_farmer={
    'FarmerID':4,
    'FarmerEmail':"harry.bratch@gmail.c",
    'FarmerName': "Harry Bratch",
    'FarmerPassword': "passcode"
    }

cursor.execute(add_farmer, data_farmer)

cnx.commit()

cursor.close()

cnx.close()
