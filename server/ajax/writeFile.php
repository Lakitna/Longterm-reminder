<?php
$folder = "../data";
$file = $folder."/".$_POST['file'];
$cont = $_POST['content'];

if (!file_exists($folder)) {
    mkdir($folder, 0777, true);
}

$f = fopen($file, 'w+');
fwrite($f, $cont);
fclose($f);
?>
