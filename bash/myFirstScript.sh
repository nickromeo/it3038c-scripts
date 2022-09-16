greeting="this is a script by the man. Hello"
echo $greeting
echo 'sha-bang'
echo Machine Type: $MACHTYPE
a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo My Ip is $a
