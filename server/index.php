<?php
$date = getdate();

if ($_GET['key'] == 'ToRz1XwK5ux4DZ5t6QPJ71ym@5fO647bQT^D7exs') {
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
	}
}


<?php
}
else { echo 'Invalid key'; }
?>