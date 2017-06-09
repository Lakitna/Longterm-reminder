<?php
@include("secrets.php");

$date = getdate();

if (isset($_GET['key'])) {
	if ($_GET['key'] == $secrets_api_key) {
		if (!isset($_GET['edit'])) {
			?>
				{
					"date": {
						"y": <?php echo $date['year']; ?>,
						"m": <?php echo $date['mon']; ?>,
						"d": <?php echo $date['mday']; ?>
					},
					"time": {
						"h": <?php echo $date['hours']; ?>,
						"m": <?php echo $date['minutes']; ?>
					},
					"content":
						<?php echo getFile("content.json"); ?>
				}
			<?php
		}
		else {
			?>
				<textarea style="width: 100%; height: 600px;"><?php
					$file = json_decode(getFile("content.json"), true);
					$revision = json_decode("{".$_GET['edit']."}", true);

					foreach ($revision as $item_rev_key => $item_rev_val) { 			// Each item code in revision
						foreach ($file[$item_rev_key] as $file_key => $file_val) { 		// Each current attribute of item in
							foreach($revision[$item_rev_key] as $rev_key => $rev_val) { // Each attribute in revision
								if ($file_key == $rev_key) {							// If revision attribute key is already present
									if (gettype($rev_val) != "array") {					// If not an array do simple replace
										$file[$item_rev_key][$file_key] = $rev_val;		// Replace
									}
									else {												// If it is an array, do an array merge
										$file[$item_rev_key][$file_key] = array_merge($file[$item_rev_key][$file_key], $rev_val);
									}
								}
							}
						}
					}


					$newfile = json_encode($file, true);
					print_r($newfile);

					$f = fopen("content.json", 'w+');
					fwrite($f, $newfile);
					fclose($f);
				?></textarea>
				<input type="button" value="Submit">
			<?php
		}
	}
	else { key_error(); }
}
else { key_error(); }


function getFile($file) {
	$f = fopen($file, 'r');
	$content = fread($f, filesize($file));

	return $content;

	fclose($f);
}

function key_error() {
	echo 'ERR: Invalid API key';
}
?>
