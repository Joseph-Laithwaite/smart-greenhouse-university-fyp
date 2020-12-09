<!-- menu.php -->
<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
<style>
ul {
   list-style-type: none;
   margin: 0;
   padding: 0;
   overflow: hidden;
   background-color: #333;
}

li {
   float: left;
}

li a, .dropbtn {
   display: inline-block;
   color: white;
   text-align: center;
   padding: 14px 16px;
   text-decoration: none;
}

li a:hover, .dropdown:hover .dropbtn {
   background-color: #69ff33;
}

li.dropdown {
   display: inline-block;
}

.dropdown-content {
   display: none;
   position: absolute;
   background-color: #f9f9f9;
   min-width: 160px;
   box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
   z-index: 1;
}

.dropdown-content a {
   color: black;
   padding: 12px 16px;
   text-decoration: none;
   display: block;
   text-align: left;
}

.dropdown-content a:hover {background-color: #f1f1f1}

.dropdown:hover .dropdown-content {
   display: block;
}
</style>
</head>
<body>
<ul>
 <li><a href="/smart_farm/welcome_page.php">Home</a></li>
   <li class="dropdown">
       <a href="javascript:void(0)" class="dropbtn">Data</a>
       <div class="dropdown-content">
           <a href="/smart_farm/data/Multi_Series_Luminosity.php">Light Module</a>
           <a href="/smart_farm/data/Multi_Series_Temperature.php">Temperature Module</a>
           <a href="/smart_farm/data/Multi_Series_Humidity.php">Humidity Module</a>
           <a href="/smart_farm/data/Multi_Series_Water_Module.php">Water Module</a>
           <a href="">pH Module</a>
       </div>

 <li><a href="Add_Installed_Sensors_2.php">Settings</a></li>
 <li style="float:right"><a href="/smart_farm/smart_farm_login.php">Log Out</a></li>
 <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Add/Edit hardware config</a>
   <div class="dropdown-content">
     <a href="/smart_farm/edit_hardware/add_farm.php">Add Farm</a>
     <a href="/smart_farm/edit_hardware/edit_region.php">Add/ Edit Region</a>
     <a href="/smart_farm/edit_hardware/edit_sensors.php">Add/ Edit Sensors</a>
     <a href="/smart_farm/edit_hardware/edit_correctors.php">Add/ Edit Correctors</a>
     <a href="/smart_farm/edit_hardware/edit_modules.php">Add/ Edit Modules</a>
   </div>

 <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Regions</a>
   <div class="dropdown-content">
     <a href="#">Region 1</a>
     <a href="#">Region 2</a>
     <a href="#">Region 3</a>
   </div>
 </li>
 <li style="float:right"><a class="active"><?php echo $_SESSION["farmerName"] ?></a></li>
</ul>

</body>
</html>
