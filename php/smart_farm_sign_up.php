<!-- smart_farm_sign_up.php -->
<?php
session_start();
require 'sql_query_and_insertion.php';
require 'useful_functions.php';
?>


<!DOCTYPE HTML> 
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body> 


<?php
// define variables and set to empty values

$farmerEmail = $farmerName = $farmerPassword = $farmerPassword1 = $farmerPassword2 = "";
$nameErr = $emailErr = $passwordErr = $tempPassword ="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
 if (empty($_POST["farmerName"])) {
   $nameErr = "Name is required";
 } else {
   $farmerName = test_input($_POST["farmerName"]);
   // check if farmerName only contains letters and whitespace
   if (!preg_match("/^[a-zA-Z ]*$/",$farmerName)) {
     $nameErr = "Only letters and white space allowed";
   }
 }

 if (empty($_POST["farmerEmail"])) {
   $emailErr = "Email is required";
 } else {
   $farmerEmail = test_input($_POST["farmerEmail"]);
   // check if e-mail address is well-formed
   if (!filter_var($farmerEmail, FILTER_VALIDATE_EMAIL)) {
     $emailErr = "Invalid email format";
   }
 }

 if (empty($_POST["farmerPassword1"])) {
   $passwordErr = "Password is required";
 } else {

  $tempPassword = preg_replace('/\s+/', '', test_input($_POST["farmerPassword1"]));

  if($_POST["farmerPassword1"] == $tempPassword){
         if ($farmerPassword1 == $farmerPassword2){
            //echo password_hash($tempPassword, PASSWORD_BCRYPT);
            $farmerPassword = password_hash($tempPassword, PASSWORD_BCRYPT);
         }else{
            $passwordErr = $passwordErr = "Passwords must match";
          }
   }else{
         $passwordErr = "No white spaces allowed";
  }
 }
 //echo "Ready to write to db";

 if (($nameErr=="") && ($emailErr=="") && ($passwordErr=="")){
  
   echo "Ready to write to db<br>";
   //Add the submitted data to the Farmer tuple in SmartGreenhouse SQL db
  
   try {
      $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
      // set the PDO error mode to exception
      $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  echo "Connection made<br>";
 
      // prepare sql and bind parameters
      $insertIntoFarmers = "INSERT INTO Farmer (FarmerName, FarmerEmail, farmerPassword)
      VALUES (:farmerName, :farmerEmail, :farmerPassword)";
     
      $stmt = $conn->prepare($insertIntoFarmers);
     
      echo "Insert Prepared<br>";
     
      $stmt->bindParam(':farmerName', $farmerName);
      $stmt->bindParam(':farmerEmail', $farmerEmail);
      $stmt->bindParam(':farmerPassword', $farmerPassword);
                   
      echo "parameters bound<br>";
     
      $stmt->execute();
     
      echo "Insert Executed<br>";
     
      $last_id = $conn->lastInsertId();
      echo "New record created successfully. Last inserted ID is: " . $last_id;   
 
  $_SESSION["farmerID"] = $last_id;
  $_SESSION["farmerName"] = $farmerName;
  header('location: /smart_farm/welcome_page.php');
 
  }

   catch(PDOException $e)
      {
      echo "Error: " . $e->getMessage();
      }
  $conn = null;
 
 }

}


?>

<h2>Farmer sign-up form</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
 Name: <input type="text" name="farmerName" value="<?php echo $farmerName;?>">
 <span class="error">* <?php echo $nameErr;?></span>
 <br><br>
 E-mail: <input type="text" name="farmerEmail" value="<?php echo $farmerEmail;?>">
 <span class="error">* <?php echo $emailErr;?></span>
 <br><br>
 Password: <input type="password"  name="farmerPassword1" value="<?php echo $farmerPassword1;?>">
 <span class="error">* <?php echo $passwordErr;?></span>
 <br><br>
 Re-enter password: <input type="password"  name="farmerPassword2" value="<?php echo $farmerPassword2;?>">
 <span class="error">* <?php echo $passwordErr;?></span>

 <br><br>

 <input type="submit" name="submit" value="Submit"> 
</form>



</body>
</html>

