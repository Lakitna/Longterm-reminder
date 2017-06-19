<?php
@include("secrets.php");
@include("include/fileHandling.php");

if ($GLOBALS["secrets_api_key"] == $_GET['key']) { // If key correct
    if (isset($_GET['edit'])) {
        // Edit mode
        if (strlen($_GET['edit']) > 0) {
            // Revision command
            updateDataFile($_GET['edit']);
        }
        else {
            // Revision ui
            @include("include/webui.php");
        }
    }
    else {
        // Not edit mode
        echo output();
    }
}
else {
    die("Invalid key");
}




function updateDataFile($revision) {
    $file     = grabJsonFile($GLOBALS["secrets_data_file"]) or die("File error");
    $revision = json_decode($revision, true) or die("JSON error");

    $merge = array_replace_recursive($file, $revision);
    $merge = json_encode($merge, JSON_FORCE_OBJECT);

    echo writeFile($GLOBALS["secrets_data_file"], $merge);
}

function output() {
    $ret = json_decode(JSONtimestamp(), true) or die("JSON error");
    $ret['content'] = grabJsonFile($GLOBALS["secrets_data_file"]);

    return json_encode($ret, JSON_FORCE_OBJECT);
}

function JSONtimestamp() {
    $date = getdate();

    return '{"now":{'.
                '"Y":'.$date['year'].','.
                '"M":'.$date['mon'].','.
                '"D":'.$date['mday'].','.
                '"h":'.$date['hours'].','.
                '"m":'.$date['minutes'].
           '}}';
}
?>
