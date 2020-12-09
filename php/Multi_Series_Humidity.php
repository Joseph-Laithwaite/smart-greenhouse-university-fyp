<!-- Multi_Series_Humidity.php -->
<?php

require  '../menu.php';
include("wrappers 2/php-wrapper/fusioncharts.php");

// Database Info

$hostdb = "localhost";  // MySQl host
$userdb = "joseph";  // MySQL username
$passdb = "passcode";  // MySQL password
$namedb = "SmartGreenhouse_2";  // MySQL database name


// Establish a connection to the database
$dbhandle = new mysqli($hostdb, $userdb, $passdb, $namedb);

/*Render an error message, to avoid abrupt failure, if the database connection parameters are incorrect */
if ($dbhandle->connect_error) {
   exit("There was an error with your connection: ".$dbhandle->connect_error);
}
?>

<html>

<head>
   <title>Humidity Chart</title>
   <script src="http://static.fusioncharts.com/code/latest/fusioncharts.js"></script>
   <script src="http://static.fusioncharts.com/code/latest/fusioncharts.charts.js"></script>
   <script src="http://static.fusioncharts.com/code/latest/themes/fusioncharts.theme.zune.js"></script>
</head>

<body>


<?php

$categoryArray=array();
$arrData = array(
   "chart" => array(
      "caption"=> "Humidity module",
      "pYAxisName"=> "Relative Humidty % of water air saturation",
      "sYAxisName"=> "Fan State (1 is on and 0 is off)",
      "xAxisHumidname"=> "Date time",
      "pixelsPerPoint"=> "0",
      "lineThickness"=> "1",
      "pAxisMinValue"=>"0",
      "pAxisMaxValue"=>"100",
      "sYAxisMinValue"=> "0",
      "theme"=> "zune"
   )
);

$strxAxisHumidQuery = "
SELECT  
  TimeStampStart AS `TimeStamp`
  from   CorrectionAction UNION ALL SELECT   TimeStampEnd AS `TimeStamp` from   CorrectionAction WHERE  
InstalledCorrectors_CorrectorID = '4'          UNION ALL       SELECT      `TimeStamp`   
FROM      SensorReadings    WHERE      InstalledSensors_SensorID = '7'      OR InstalledSensors_SensorID = '8'
   UNION ALL    SELECT      DISTINCT *    FROM      (        SELECT          ConditionStartTime       
from          DesiredConditions        WHERE          CorrectionModule_ModuleID = '4'        UNION ALL
       SELECT          ConditionEndTime        from          DesiredConditions        WHERE     
   CorrectionModule_ModuleID = '4'      ) correctionTimes order by  `TimeStamp` ASC";

$result = $dbhandle->query($strxAxisHumidQuery.";") or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");

if ($result) {
   // pushing category array values
   $count = 0;
   while($row = mysqli_fetch_array($result)) {
       array_push($categoryArray, array(
           "label" => $row["TimeStamp"]));
   }
}

$sensor1Readings=array();

$strQuery = "
SELECT
 SensorValue
FROM
 (
   (".$strxAxisHumidQuery.") sr1
   LEFT JOIN (
     SELECT
       `TimeStamp`,
       SensorValue
     FROM
       SensorReadings
     WHERE
       InstalledSensors_SensorID = '7'
   ) sr2 ON sr1.`TimeStamp` = sr2.`TimeStamp`
 )
ORDER BY
 sr1.`TimeStamp` ASC;
";

$result = $dbhandle->query($strQuery) or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");
if ($result) {
   // pushing category array values
   $lastValue=0;
   while($row = mysqli_fetch_array($result)) {
       if ($row["SensorValue"] === null or (float)$row["SensorValue"] < 0){
           array_push($sensor1Readings, array("value" => ((float)$lastValue )));
       }
       else{
           array_push($sensor1Readings, array("value" => ((float)$row["SensorValue"])));
           $lastValue = $row["SensorValue"];
       }

   }
}

$dbhandle->close();

$sensor2Readings=array();

$strQuery = "
SELECT
 SensorValue
FROM
 (
   (".$strxAxisHumidQuery.") sr1
   LEFT JOIN (
     SELECT
       `TimeStamp`,
       SensorValue
     FROM
       SensorReadings
     WHERE
       InstalledSensors_SensorID = '8'
   ) sr2 ON sr1.`TimeStamp` = sr2.`TimeStamp`
 )
ORDER BY
 sr1.`TimeStamp` ASC;
";
$dbhandle->close();
$dbhandle = new mysqli($hostdb, $userdb, $passdb, $namedb);

$result = $dbhandle->query($strQuery) or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");
if ($result) {
   $lastValue=0;
   while($row = mysqli_fetch_array($result)) {
       if ($row["SensorValue"] === null or (float)$row["SensorValue"] < 0){
           array_push($sensor2Readings, array("value" => ((float)$lastValue )));
       }
       else{
           array_push($sensor2Readings, array("value" => ((float)$row["SensorValue"])));
           $lastValue = $row["SensorValue"];
       }

   }
};


$correctionActions=array();


$strQuery = "SELECT
 caOn.TimeStampStart AS CorrectionStart,
 caOff.TimeStampEnd AS CorrectionEnd
FROM
 (
   xAxisHumid
   LEFT JOIN (
     SELECT
       *
     FROM
       CorrectionAction
     WHERE
       InstalledCorrectors_CorrectorID = '4'
   ) caOn ON xAxisHumid.`TimeStamp` = caOn.TimeStampStart
 )
 LEFT JOIN (
   SELECT
     *
   FROM
     CorrectionAction
   WHERE
     InstalledCorrectors_CorrectorID = '4'
 ) caOff ON xAxisHumid.`TimeStamp` = caOff.TimeStampEnd;
";

$dbhandle->close();

$dbhandle = new mysqli($hostdb, $userdb, $passdb, $namedb);

$result = $dbhandle->query($strQuery) or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");

if ($result) {
   $lastValue=0;
   while($row = mysqli_fetch_array($result)) {
       if ($row["CorrectionStart"] !== null){
           array_push($CorrectionActions, array("value" => 1 ));
           $lastValue = 1;
       }
       elseif ($row["CorrectionEnd"] !== null){
           array_push($correctionActions, array("value" => 0));
           $lastValue = 0;
       }
       else{
           array_push($correctionActions, array("value" => $lastValue));
       }
   }
};



$dbhandle->close();

$dbhandle = new mysqli($hostdb, $userdb, $passdb, $namedb);
$arrData["categories"]=array(array("category"=>$categoryArray));
// creating dataset object
$arrData["dataset"] = array(
       array(
           "seriesName"=> "Internal Relative Humidity",
           "parentyaxis"=> "p",
           "renderAs"=>"line",
           "data"=>$sensor1Readings),
       array(
           "seriesName"=> "External Relative Humidity",
           "parentyaxis"=> "P",
           "renderAs"=>"line",
           "data"=>$sensor2Readings),
       array(
           "seriesName"=> "Fan On",
           "parentyaxis"=> "S",
           "renderAs"=>"line",
           "data"=>$correctionActions)
);

/*JSON Encode the data to retrieve the string containing the JSON representation of the data in the array. */
$jsonEncodedData = json_encode($arrData);

//echo $jsonEncodedData;

// chart object
$msChart = new FusionCharts(
       "zoomlinedy",
       "chart1" ,
       1000, 600,
       "chart-container",
       "json",
       $jsonEncodedData);


// Render the chart
$msChart->render();


$dbhandle->close();


?>

<center>
   <div id="chart-container">Humidity Chart will render here!</div>
</center>
</body>

</html>

