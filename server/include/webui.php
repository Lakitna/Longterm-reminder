<html>
<head>
    <title>Long term reminder</title>

    <script
      src="https://code.jquery.com/jquery-3.2.1.min.js"
      integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
      crossorigin="anonymous"></script>
    <script src="js/ajax.js"></script>
    <script>
        $(document).ready(function() {
            $("#sub_but").click(function() {
                var obj = $("textarea");
                var data = obj.val();
                data = JSON.parse(data);
                data = JSON.stringify(data);

                console.log(data);

                keyValidation(<?php echo "\"".$_GET['key']."\""; ?>, function(fn) {
                    updateFileContent(fn, data, function(code) {
                        console.log(code);
                        if (code == 1) {
                            obj.val("Saved");
                        }
                        else {
                            obj.val("Error");
                        }
                    });
                });
            });
            $("#add_but").click(function() {
                var obj = $("textarea");
                var data = obj.val();
                data = JSON.parse(data);
                var key = Object.keys(data).length;

                data[key] = <?php echo getFile("data/template.json") ?>;
                data = JSON.stringify(data, null, 4);

                obj.text(data);
            });
        });
    </script>
</head>
<body>

    <textarea cols="200" rows="50"><?php
        $data = getFile("data/".$GLOBALS["secrets_data_file"]);
        $data = json_decode($data);
        $data = json_encode($data, JSON_PRETTY_PRINT);
        echo $data;
    ?></textarea>
    <button id="sub_but">Submit</button>
    <button id="add_but">Add item</button>

</body>
</html>
