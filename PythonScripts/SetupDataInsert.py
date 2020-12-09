import mysql.connector
from mysql.connector import errorcode


config={
    'user':'joseph',
    'password':'passcode',
    'host':'localhost',
    'database':'SmartGreenhouse',
    'raise_on_warnings':True,
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

#Insert farmer

add_farmer = ("INSERT INTO SmartGreenhouse.Farmer"
              "(FarmerEmail,FarmerName,FarmerPassword)"
              "VALUES (%(FarmerEmail)s,%(FarmerName)s,PASSWORD(\"%(FarmerPassword)s\"));"
              )

data_farmer = {
    'FarmerEmail':"joe.laith@live.com",
    'FarmerName': "Joseph Laithwaite",
    'FarmerPassword': "passcode"
    }


cursor.execute(add_farmer, data_farmer)

cnx.commit()

#Insert farm

add_farm = ("INSERT INTO SmartGreenhouse.Farm" 
           "(FarmName, FarmID, Farmer_FarmerID)"
           "VALUES(%(FarmName)s, %(FarmID)s, %(Farmer_FarmerID)s);"
           )

data_farm = {
  'FarmName': "My Farm",
  'FarmID': 1,
  'Farmer_FarmerID': 1,
}


cursor.execute(add_farm, data_farm)

cnx.commit()

#insert farm region

add_farm_region = ("SmartGreenhouse.FarmRegion" 
                  "(RegionID, FarmRegionName, RegionDescription, Farm_FarmID)
                  "VALUES(%(RegionID)s, %(FarmRegionName)s, %(RegionDescription)s, %(Farm_FarmID)s);"
                  )

data_farm_region = {
  'RegionID': 1,
  'FarmRegionName': "First region",
  'RegionDescription': "The small prototype greenhouse, used tp demonstrate the systems potential",
  'Farm_FarmID': 1,
}  

cursor.execute(add_farm_region, data_farm_region)

cnx.commit()

#Insert Sensor types

add_sensor_type = ("SmartGreenhouse.SensorTypes" 
                  "(SensorTypeID, SensorName)"
                  "VALUES(%(SensorTypeID)s, %(SensorName)s, %(SensorUnit)s)"

data_sensor_type = {
  'SensorTypeID': 1,
  'SensorName': "Air Temperature",
  'SensorUnit': "°C",
}

cursor.execute(add_sensor_type, data_sensor_type)

cnx.commit()

data_sensor_type = {
  'SensorTypeID': 2,
  'SensorName': "Humidity",
  'SensorUnit': "%",
}

cursor.execute(add_sensor_type, data_sensor_type)

cnx.commit()

data_sensor_type = {
  'SensorTypeID': 3,
  'SensorName': "Luminosity",
  'SensorUnit': "Lux",
}

cursor.execute(add_sensor_type, data_sensor_type)

cnx.commit()

data_sensor_type = {
  'SensorTypeID': 4,
  'SensorName': "PH",
  'SensorUnit': "ph",
}

cursor.execute(add_sensor_type, data_sensor_type)

cnx.commit()

data_sensor_type = {
  'SensorTypeID': 5,
  'SensorName': "Water Volume",
  'SensorUnit': "ml",
}

cursor.execute(add_sensor_type, data_sensor_type)

cnx.commit()

add_installed_sensors = ("SmartGreenhouse.InstalledSensors"
                        "(SensorID, FarmRegion_RegionID, SensorTypeID, SensorTypes_SensorTypeID)"
                        "VALUES(%(SensorID)s, %(FarmRegion_RegionID)s, %(SensorTypes_SensorTypeID)s, %(SensorNickname)s);"
                        )

data_installed_sensors = {
  'SensorID':1, 
  'FarmRegion_RegionID':1, 
  'SensorTypes_SensorTypeID':1,
  'SensorNickname':"Internal Temperature",
}

cursor.execute(add_installed_sensor, data_installed_sensor)

cnx.commit()

data_installed_sensors = {
  'SensorID':2, 
  'FarmRegion_RegionID':1, 
  'SensorTypes_SensorTypeID':3,
  'SensorNickname': "Internal light level",
}

cursor.execute(add_installed_sensor, data_installed_sensor)

cnx.commit()

data_installed_sensors = {
  'SensorID':3, 
  'FarmRegion_RegionID':1, 
  'SensorTypes_SensorTypeID':3,
  'SensorNickname': "External light level",
}

cursor.execute(add_installed_sensor, data_installed_sensor)

cnx.commit()

data_installed_sensors = {
  'SensorID':4, 
  'FarmRegion_RegionID':1, 
  'SensorTypes_SensorTypeID':4,
  'SensorNickname':"Water reservoir PH",
}

cursor.execute(add_installed_sensor, data_installed_sensor)

cnx.commit()

data_installed_sensors = {
  'SensorID':5, 
  'FarmRegion_RegionID':1, 
  'SensorTypes_SensorTypeID':5,
  'SensorNickname':"Water reservoir volume",
}

cursor.execute(add_installed_sensor, data_installed_sensor)

cnx.commit()


cursor.close()

cnx.close()
