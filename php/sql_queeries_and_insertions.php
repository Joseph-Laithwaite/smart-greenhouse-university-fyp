<!-- sql_queeries_and_insertions.php -->
<?php

// Database Info

 $servername = "localhost";
 $username = "joseph";
 $password = "passcode";
 $dbname = "SmartGreenhouse_2";

 $insertIntoFarmers =
      "INSERT INTO Farmer (FarmerName, FarmerEmail, farmerPassword)
      VALUES (:farmerName, :farmerEmail, :farmerPassword)";

 $selectAllFromFarmerWHereEmail =
      "SELECT farmerID, FarmerEmail, FarmerName, farmerPassword
        FROM Farmer
         WHERE FarmerEmail = :farmerEmail";

 $querry_for_sensor_data =
       "SELECT TimeStamp, SensorValue
         FROM SensorReadings
         WHERE InstalledSensors_SensorID = :sensor_id AND TimeStamp >= :start_time
        ORDER BY TimeStamp DESC
       ";
$querry_last_sensor_data =
       "SELECT SensorValue
         FROM SensorReadings
         WHERE InstalledSensors_SensorID = :sensor_id
        ORDER BY TimeStamp DESC
        LIMIT 1
       ";
$query_for_regions=
      "SELECT FarmRegionName, RegionID
       FROM FarmRegion
       WHERE Farm_FarmID = :FarmID
      ";
$query_for_farms=
     "SELECT FarmName, FarmID
      FROM Farm
      WHERE Farmer_FarmerID = :FarmerID
      ";
$insert_into_farms =
      "INSERT INTO Farm (FarmName, Farmer_FarmerID)
       VALUES (:farmName, :farmerID)
      ";
   $query_for_sensors=
       "SELECT SensorNickname, SensorID
       FROM InstalledSensors
       WHERE RegionID = :RegionID  
       ";
?>
