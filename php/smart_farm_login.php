<!-- smart_farm_login.php -->
<?php
session_start();
require 'sql_query_and_insertion.php';
require 'useful_functions.php';
$_SESSION["farmerID"] = 0;
$_SESSION["farmerName"] ="";
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

$farmerEmail = $farmerPasswordInput = "";
$emailErr = $passwordErr ="";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
   switch ($_POST["submit"]) {
       case "Sign-in":

           if (empty($_POST["farmerPasswordInput"])) {
               $passwordErr = "Password is required";
           }
           if (empty($_POST["farmerEmail"])) {
               $emailErr = "Email is required";
           }

           //echo "Ready to write to db";

           if (($emailErr=="") && ($passwordErr=="")){
               $farmerEmail = test_input($_POST["farmerEmail"]);
               $farmerPasswordInput = test_input($_POST["farmerPasswordInput"]);
               echo "Ready to get user info from db<br>";
               //Get the users data corresponding to the given email from the Farmer table in SmartGreenhouse SQL db

               try {
                   $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);

                   // set the PDO error mode to exception

                   $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                   echo "Connection made<br>";

                   // prepare sql and bind parameters

                   echo "SQL Select statement made<br>";

                   $stmt = $conn->prepare($selectAllFromFarmerWHereEmail);

                   echo "parameters Prepared<br>";

                   $stmt->execute([':farmerEmail' => $farmerEmail]);

                   echo "querry executed <br>";

                   while ($userInfo = $stmt->fetch(PDO::FETCH_ASSOC)){
                       $_SESSION["farmerID"] = $userInfo[farmerID];
                       $_SESSION["farmerName"] = $userInfo[FarmerName];
                       $hash = $userInfo[farmerPassword];
                   }
                   if (password_verify($farmerPasswordInput, $hash)){
                       header('location: /smart_farm/welcome_page.php');
                   }else{
                       $emailErr = $passwordErr = "password & email do not match";
                   }
               }
               catch(PDOException $e)
               {
                   echo "Error: " . $e->getMessage();
               }
               $conn = null;
           }
           break;
       case "sign-up":
           header('location: /smart_farm/smart_farm_sign-up.php');
           break;
   }


}
?>

<h2>Farmer sign-in form</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">

   E-mail: <input type="text" name="farmerEmail" value="<?php echo $farmerEmail;?>">
   <span class="error">* <?php echo $emailErr;?></span>
   <br><br>
   Password: <input type="password"  name="farmerPasswordInput" value="<?php echo $farmerPasswordInput;?>">
   <span class="error">* <?php echo $passwordErr;?></span>
   <br><br>

   <input type="submit" name="submit" value="Sign-in">
</form>

<br><br>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
   <input type="submit" name="submit" value="sign-up">
</form>

</body>
</html>

