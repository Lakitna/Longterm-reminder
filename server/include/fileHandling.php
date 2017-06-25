<?php
function writeFile($file, $cont) {
    $folder = "data";
    $file = $folder."/".$file;

    if (!file_exists($folder)) {
        mkdir($folder, 0777, true);
    }

    $f = fopen($file, 'w+');
    fwrite($f, $cont);
    fclose($f);

    return "Success";
}

function getFile($file) {
    $f = fopen($file, 'r');
    $content = fread($f, filesize($file));
    fclose($f);
    return $content;
}

function grabJsonFile($file) {
    return json_decode( getFile("data/".$file), true );
}

?>
