<!-- useful_functions.php -->
<?php

function test_input($data) {
 $data = trim($data);
 $data = stripslashes($data);
 $data = htmlspecialchars($data);
 return $data;
}

function get_db_connection(){
   require 'sql_query_and_insertion.php';
   try{
     //echo "About to attempt to connect<br>";
  $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
     //echo "Connected<br>";
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
     //echo "Set up <br>";
  return $conn;
   }
   catch(PDOException $e) {
      echo "Error: " . $e->getMessage();
      return NULL;
   }
}



function get_sensor_data($sensor_id, $start_time){
  echo "Getting sensor data<br>";
  require 'sql_query_and_insertion.php';
 
 
  echo "<table style='border: solid 1px black;'>";
  echo "<tr><th>Time</th><th>Sensor Reading</th></tr>";

  class TableRows extends RecursiveIteratorIterator {
      function __construct($it) {
          parent::__construct($it, self::LEAVES_ONLY);
      }
      function current() {
          return "<td style='width:150px;border:1px solid black;'>" . parent::current(). "</td>";
      }
      function beginChildren() {
          echo "<tr>";
      }
      function endChildren() {
          echo "</tr>" . "\n";
      }
  }
 
 
  try {
      $conn = get_db_connection();
      $stmt = $conn->prepare($querry_for_sensor_data);
      $stmt->execute([':sensor_id' => $sensor_id, ':start_time' => $start_time]);   
      // set the resulting array to associative
      $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
      foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v) {
          echo $v;
      }
  }
  catch(PDOException $e) {
      echo "Error: " . $e->getMessage();
  }
  $conn = null;
  echo "</table>";
}


function get_last_sensor_data($sensor_id){
  require 'sql_query_and_insertion.php';
  $conn = get_db_connection();
  $stmt = $conn->prepare($querry_last_sensor_data);
  $stmt->execute([':sensor_id' => $sensor_id]);    

  $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
 
  echo $result;
}
 
 
  function display_farm_combo($farmer_id, $selectedID=0) {
  require 'sql_query_and_insertion.php';
  $conn = get_db_connection();
  $stmt = $conn->prepare($query_for_farms);
  $stmt -> execute([':FarmerID' => $farmer_id]);
  echo "<select name = \"farmNameSelect\" >";
  echo "  <option  value = \"Add new farm\">Add new farm</option>";
  while ($farmInfo = $stmt->fetch(PDO::FETCH_ASSOC)){
     echo "<option value = \"" ;
     echo $farmInfo["FarmID"];
           echo "\"";
     if ($farmInfo["FarmID"] == $selectedID){
        echo " selected ";   
     }
     echo ">";
     echo $farmInfo["FarmName"];
     echo "</option>";
  }
  echo "</select>";
}

function display_region_combo($farm_id, $selectedID=0) {
  require 'sql_query_and_insertion.php';
  $conn = get_db_connection();
  $stmt = $conn->prepare($query_for_regions);
  $stmt -> execute([':FarmID' => $farm_id]);
  echo "<br>";  
  echo "<select name = \"regionNameSelect\" >";
  echo "  <option  value = \"Add new region\">Add new region</option>";
  while ($region_info = $stmt->fetch(PDO::FETCH_ASSOC)){
     echo "<option value = \"" ;
     echo $region_info["RegionID"];
     echo "\"";
     if ($region_info["RegionID"] == $selectedID){
        echo " selected ";   
     }
     echo ">";
     echo $region_info["FarmRegionName"];
     echo "</option>";
  }
  echo "</select>";
}

function display_sensor_combo($farm_id, $region_id) {
   require 'sql_query_and_insertion.php';
   $conn = get_db_connection();
   $stmt = $conn->prepare($query_for_sensors);
   $stmt -> execute([':FarmID' => $farm_id, ':RegionID' => $region_id]);
   echo "<br>";
   echo "<select name = \"sensorNameSelect\" >";
   echo "  <option  value = \"Add new sensor\">Add new sensor</option>";
   while ($sensor_info = $stmt->fetch(PDO::FETCH_ASSOC)){
       echo "<option value = \"" ;
       echo $sensor_info["RegionID"];
       echo "\"";
//        if ($sensor_info["RegionID"] == $selectedID){
//            echo " selected ";
//        }
       echo ">";
       echo $sensor_info["FarmRegionName"];
       echo "</option>";
   }
   echo "</select>";
}


function add_farm($farmName, $farmerID){
  require 'sql_query_and_insertion.php';
  try {
      $conn = get_db_connection();
     //echo "Connection made<br>";
     $stmt = $conn->prepare($insert_into_farms);
      //echo "Insert Prepared<br>";
      $stmt->execute([':farmName' => $farmName, ':farmerID' => $farmerID]);
      //echo "Insert Executed<br>";
      return $FarmID = $conn->lastInsertId();
  }   
  catch(PDOException $e){
      echo "Error: " . $e->getMessage();
   } 
  $conn = null;
}

function add_region($regionName, $regionDescription, $farmID){
  require 'sql_query_and_insertion.php';
  try {
      $conn = get_db_connection();
     //echo "Connection made<br>";
     $insert_into_region = "
        INSERT INTO FarmRegion(FarmRegionName, RegionDescription, Farm_FarmID)
        VALUES (:region_name, :regionDescription, :farm_id)
        ";
     $stmt = $conn->prepare($insert_into_region);
      //echo "Insert Prepared<br>";
      $stmt->execute([':region_name' => $regionName, ':regionDescription' => $regionDescription, ':farm_id' => $farmID]);
      //echo "Insert Executed<br>";
      $RegionID = $conn->lastInsertId();
      return $RegionID;
  }   
  catch(PDOException $e){
      echo "Error: " . $e->getMessage();
   } 
  $conn = null;
}

?>
