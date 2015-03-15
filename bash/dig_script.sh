#!/bin/bash
<<'COMMENT'
dig_script.sh 
msimo - 3/14/15

A command-line tool heavily reliant on the dig command, created to learn about different DNS records.

Current features:
* Find specific record for one or more domain
* Easy to read output
* Supports rDNS

Tested on Debian 7.7, requires the dig command.

COMMENT

# ask for domain name
echo "Please enter a domain name: "
read DOMAIN
IP=$(host $DOMAIN | grep 'address' | awk '{print $4}')

while :
do
echo ""
echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
echo "Domain name: $DOMAIN"
echo "$DOMAIN's IP is : $IP"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" ; echo ""

#use flex record var
#check if valid record type
echo "1. Enter DNS record type"
echo "2. Reverse DNS"
echo "3. Change Domain"
echo "4. Print various DNS records"
echo "0. Quit" ; echo ""
read OPTION ; echo ""

case $OPTION in

	1) echo "Please enter a DNS record type: "
	read RECORDTYPE
	if [ $? -eq 0  ]
		then
		echo "====================================="
		echo "||      $RECORDTYPE records        ||"
		echo "====================================="
		dig $RECORDTYPE $DOMAIN +short	
	else
		echo "ERROR >> Please make sure the record type exists and make sure your domain is correct. (example.com)"
	fi
	;;

	2) echo "====================================="
	echo "||           Reverse DNS           ||"
	echo "====================================="
	rdnsIP=$(dig +noall +answer -x $IP | awk '{print $5}')
	fdnsIP=$(dig $rdnsIP +short)
	echo "Start IP: $IP"	
	echo "Reverse DNS Hostname/IP:  $rdnsIP" 
	echo "Forward DNS Hostname/IP: $fdnsIP"
	;;

	3) 
	echo "====================================="
	echo "Please enter a domain name: "
	read DOMAIN
	IP=$(host $DOMAIN | grep 'address' | awk '{print $4}')
	;;

	4)
	echo "====================================="
	echo "||           NS records            ||"
	echo "====================================="
	dig NS $DOMAIN +short
	echo "====================================="
	echo "||           MX records            ||"
	echo "====================================="
	dig MX $DOMAIN +short
	echo "====================================="
	echo "||           A records             ||"
	echo "====================================="
	dig A $DOMAIN +short
 	echo "====================================="
	echo "||            TXT records          ||"
	echo "====================================="
	dig TXT $DOMAIN	+short
 	echo "====================================="
	echo "||          CNAME records          ||"
	echo "====================================="
	dig CNAME $DOMAIN +short
	echo
	;;

# Testing to check if the domain is valid.
#	if [[$DOMAIN == [a-z]*[0-9][a-z][.]*]]
#	then
#		echo "$DOMAIN: Match found."
#	else
#		echo "$DOMAIN: Match not found."
#	fi
	
	0)
	break
	;;
esac
done