<?php
$proto = ['tcp','udp', 'icmp'];
$service=['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50'];
$flag = [ 'OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH' ];

$handle = fopen($argv[1], 'r');
$id = 0;
$start = $argv[2];
$end = $argv[3];
while (($buffer = fgets($handle)) !== false) {
	$el = $buffer;
	$parts = explode(',', $el);
	$parts[1] = array_search($parts[1], $proto);
	$parts[2] = array_search($parts[2], $service);
	$parts[3] = array_search($parts[3], $flag);
	for($i=12;$i<22;$i++) {
		unset($parts[$i]);
	}
	for($i=24;$i<31;$i++) {
		unset($parts[$i]);
	}
	for($i=35;$i<41;$i++) {
		unset($parts[$i]);
	}
	unset($parts[42]);

	$parts[41] = $parts[41] == 'neptune' ? 0 : 1;

	$newEl = implode(',', $parts);
	if ($id > $end) {
		return;
	}
	if ($id >= $start) {
		print($newEl);
		print("\n");
	}
	$id++;
}
if (!feof($handle)) {
	    echo "Ошибка: fgets() неожиданно потерпел неудачу\n";
		}
fclose($handle);
