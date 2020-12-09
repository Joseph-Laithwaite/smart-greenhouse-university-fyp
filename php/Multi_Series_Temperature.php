<!-- Multi_Series_Temperature.php -->
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
   <title>Temperature Chart</title>
   <script src="http://static.fusioncharts.com/code/latest/fusioncharts.js"></script>
   <script src="http://static.fusioncharts.com/code/latest/fusioncharts.charts.js"></script>
   <script src="http://static.fusioncharts.com/code/latest/themes/fusioncharts.theme.zune.js"></script>
</head>

<body>


<?php

$categoryArray=array();
$arrData = array(
   "chart" => array(
       "caption"=> "Temperature module",
       "pYAxisName"=> "Temperature in degrees celsius",
       "sYAxisName"=> "Fan State (1 is on and 0 is off)",
       "xAxisname"=> "Date time",
       "compactDataMode"=> "1",
       "pixelsPerPoint"=> "0",
       "lineThickness"=> "1",
      "pYAxisMaxValue"=> "30",
       "pYAxisMinValue"=> "10",
      "forceYAxisValueDecimals" =>"1",
      "forcesYAxisValueDecimals" =>"0",
      "sYAxisValueDecimals" =>"0",
       "sYAxisMaxValue"=> "1.5",
       "sYAxisMinValue"=> "0",
       "theme"=> "zune"
   )
);

$strXAxisQuery = "SELECT   TimeStampStart AS `TimeStamp` from   CorrectionAction UNION ALL SELECT   TimeStampEnd AS `TimeStamp` from   CorrectionAction WHERE   InstalledCorrectors_CorrectorID = '4'          UNION ALL       SELECT      `TimeStamp`    FROM      SensorReadings    WHERE      InstalledSensors_SensorID = '1'      OR InstalledSensors_SensorID = '6'    UNION ALL    SELECT      DISTINCT *    FROM      (        SELECT          ConditionStartTime        from          DesiredConditions        WHERE          CorrectionModule_ModuleID = '4'        UNION ALL        SELECT          ConditionEndTime        from          DesiredConditions        WHERE          CorrectionModule_ModuleID = '4'      ) correctionTimes order by  `TimeStamp` ASC";

$result = $dbhandle->query($strXAxisQuery.";") or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");

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
   (".$strXAxisQuery.") sr1
   LEFT JOIN (
     SELECT
       `TimeStamp`,
       SensorValue
     FROM
       SensorReadings
     WHERE
       InstalledSensors_SensorID = '1'
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
       if ($row["SensorValue"] === null or $row["SensorValue"] == 0){
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
   (".$strXAxisQuery.") sr1
   LEFT JOIN (
     SELECT
       `TimeStamp`,
       SensorValue
     FROM
       SensorReadings
     WHERE
       InstalledSensors_SensorID = '6'
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
       if ($row["SensorValue"] === null or $row["SensorValue"] == 0){
           array_push($sensor2Readings, array("value" => ((float)$lastValue )));
       }
       else{
           array_push($sensor2Readings, array("value" => ((float)$row["SensorValue"])));
           $lastValue = $row["SensorValue"];
       }

   }
};


$correctionActions=array();

$dbhandle->close();

$dbhandle = new mysqli($hostdb, $userdb, $passdb, $namedb);

$strQuery = "SELECT
 caOn.TimeStampStart AS CorrectionStart,
 caOff.TimeStampEnd AS CorrectionEnd
FROM
 (
   xAxisTemp
   LEFT JOIN (
     SELECT
       *
     FROM
       CorrectionAction
     WHERE
       InstalledCorrectors_CorrectorID = '4'
   ) caOn ON xAxisTemp.`TimeStamp` = caOn.TimeStampStart
 )
 LEFT JOIN (
   SELECT
     *
   FROM
     CorrectionAction
   WHERE
     InstalledCorrectors_CorrectorID = '4'
 ) caOff ON xAxisTemp.`TimeStamp` = caOff.TimeStampEnd;
";


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

$desiredLowerLimit=array();
$desiredUpperLimit=array();


$strQuerry1 = "
SELECT
 conditionOff.ConditionEndTime AS condition_end,
 conditionOn.ConditionStartTime AS condition_start,
 conditionOn.LowerLimit AS lower_limit,
 conditionOn.UpperLimit AS upper_limit
FROM
 (
   xAxisTemp
   LEFT JOIN (
     SELECT
       dc.ConditionStartTime,
       dc.LowerLimit,
       dc.UpperLimit
     From
       DesiredConditions dc
     WHERE
       CorrectionModule_ModuleID = '4'
   ) conditionOn ON xAxisTemp.`TimeStamp` = conditionOn.ConditionStartTime
 )
 LEFT JOIN (
   SELECT
     dc1.ConditionEndTime
   From
     DesiredConditions dc1
   WHERE
     CorrectionModule_ModuleID = '4'
 ) conditionOff ON xAxisTemp.`TimeStamp` = conditionOff.ConditionEndTime
order by
 `TimeStamp` asc;
";


$result1 = $dbhandle->query($strQuerry1) or exit("Error code ({$dbhandle->errno}): {$dbhandle->error}");


if ($result1) {
   $upperValue=0;
   $lowerValue=0;
   while($row = mysqli_fetch_array($result1)) {
       if ($row["condition_start"] !== null){
           array_push($desiredLowerLimit, array("value" => $row["lower_limit"]));
           array_push($desiredUpperLimit, array("value" => $row["upper_limit"]));
           $upperValue=$row["upper_limit"];
           $lowerValue=$row["lower_limit"];
       }
       elseif ($row["condition_end"] !== null){
           array_push($correctionActions, array("value" => 0));
           $upperValue=0;
           $lowerValue=0;
       }
       else{
           array_push($desiredLowerLimit, array("value" => $lowerValue ));
           array_push($desiredUpperLimit, array("value" => $upperValue ));
       }
   }
};


$arrData["categories"]=array(array("category"=>$categoryArray));
// creating dataset object
$arrData["dataset"] = array(
       array(
           "seriesName"=> "ExternalTemperature Degrees celsius",
           "parentyaxis"=> "p",
           "renderAs"=>"line",
           "data"=>$sensor1Readings),
       array(
           "seriesName"=> "Internal  Temperature Degrees celsius",
           "parentyaxis"=> "P",
           "renderAs"=>"line",
           "data"=>$sensor2Readings),
       array(
           "seriesName"=> "Desired upper temp",
           "parentyaxis"=> "p",
           "renderAs"=>"line",
           "data"=>$desiredUpperLimit),
       array(
           "seriesName"=> "Desired lower temp",
           "parentyaxis"=> "p",
           "renderAs"=>"line",
           "data"=>$desiredLowerLimit),
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
   <div id="chart-container">Chart will render here!</div>
</center>
</body>

</html>

