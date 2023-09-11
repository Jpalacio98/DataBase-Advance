<?php

header('Access-Control-Allow-Origin: *');
header("Access-Control-Allow-Methods: HEAD, GET, POST, PUT, PATCH, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method,Access-Control-Request-Headers, Authorization");
header('Content-Type: application/json');
$method = $_SERVER['REQUEST_METHOD'];
if ($method == "OPTIONS") {
header('Access-Control-Allow-Origin: *');
header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method,Access-Control-Request-Headers, Authorization");
header("HTTP/1.1 200 OK");
die();
}


    require "config.php";
    $id = $_POST['id'];
    $nombre = $_POST['nombre'];   
    $nombre_user = $_POST['nombre_user'];
    $email = $_POST['email'];
    $contraseña = $_POST['contraseña'];
    $foto = addslashes(file_get_contents($_FILES['foto']['tmp_name']));
    /*
    $nombre = $_POST['nombre'];   
    $foto = $_POST['foto'];
    $placa = $_POST['placa'];   
    $telefono = $_POST['telefono'];  
    $whatsapp = $_POST['whatsapp'];  
    $moto = $_POST['moto'];  
    $soat = $_POST['soat'];  
    $tecno = $_POST['tecno'];  
    $activo = $_POST['activo'];  
  */
  
  
   /* 
    $nombre ='alex';   
    $foto = "alex";   
    $placa ="alex";   
    $telefono = "alex";   
    $whatsapp ="alex";   
    $moto = "alex";   
    $soat = "alex";   
    $tecno ="alex";   
    $activo = "alex";   
   
    $nombre = 'jose';   
    $nombre_user ='joaw_user';
    $email = 'email@gmail.com';
    $contraseña = 'contraseña';
     */
    $sql = "INSERT INTO Usuarios (id,nombre,nombre_user,email,contraseña,foto) VALUES (default,'$nombre', '$nombre_user', '$email','$contraseña',' $foto)";
    
    if (mysqli_query($con, $sql)) {
    $respuesta = array("mensaje"=>"Datos Modificados");
    $json_string = json_encode($respuesta);
    echo $json_string;
  } else {
    $respuesta = array("mensaje"=>"Error". mysqli_error($con));
    $json_string = json_encode($respuesta);
    echo $json_string;
  }
    
?>
