<?php
$file = "../data/".$_POST['file'];

if (file_exists($file) == false) {
    die("0");
}

$f = fopen($file, 'r');
$content = fread($f, filesize($file));

echo $content;
fclose($f);
?>
