<!-- welcome_page.php -->
<?php
session_start();
include 'menu.php';
include 'sql_query_and_insertion.php';
include 'useful_functions.php';
?>

<!DOCTYPE HTML> 
<html>
<head>
<h1>Welcome to your smart farm interface</h1>
</head>
<body>

<?php

echo "Hello, " . $_SESSION["farmerName"] . ". <br>Your ID is " . $_SESSION["farmerID"];

//get_sensor_data('1', '2018-02-13 09:20:00');


//get_last_sensor_data('1');


?>

</body>
</html>