function getIP { 
(Get-NetIPAddress).ipv4address | Select-String "192"
}
function getHost{ hostname
}
function getVer{ $host.Version 
}
function date{ Get-Date }

$IP = getIP
$NAME = getHost
$VER = getVer
$DATE = date
$Body = "this machines IP is $IP, this machine name is $NAME, this machine's powershell verion is $VER, Todays date is $DATE"
