<?php

session_start();
$host = "localhost"; /* equipo */
$user = "id18968232_jpalacio21"; /* usuario */
$password = "@1119840949Jp"; /* clave */
$dbname = "id18968232_bd_avanzada"; /* base de datos */

$con = mysqli_connect($host, $user, $password,$dbname);

if (!$con) {
  die("Connection failed: " . mysqli_connect_error());
}
//echo "Conexion Exitosa";

?>
