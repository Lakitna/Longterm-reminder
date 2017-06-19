<?php
@include("../secrets.php");

if ($_POST['key'] == $secrets_api_key) {
    // Make data file if it doesn't exist and fill with empty object
    if (file_exists("../data/".$secrets_data_file) == false) {
        $file = fopen("../data/".$secrets_data_file, "w") or die("Unable to open file!");
        fwrite($file, "{}");
        fclose($file);
    }

    echo $secrets_data_file;
}
else {
    die("0");
}
?>
