function updateFileContent(fileName, content, callback) {
    $.ajax({
        type: "POST",
        url: "ajax/writeFile.php",
        data: { "file": fileName, "content": content }
    })
    .done(function() {
        callback(1);
    })
    .fail(function() {
        callback(0);
    });

}

function getFileContent(fileName, callback) {
    $.ajax({
        type: "POST",
        url: "ajax/getFile.php",
        data: { "file": fileName }
    })
    .done(function(ret) {
        callback(ret);
    })
    .fail(function() {
        callback(0);
    });
}


function keyValidation(key, callback) {
    $.ajax({
        type: "POST",
        url: "ajax/keyValidation.php",
        data: { "key": key }
    })
    .done(function(ret) {
        callback(ret);
    })
    .fail(function() {
        callback(0);
    });
}
