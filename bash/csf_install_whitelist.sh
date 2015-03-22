#!/bin/bash
#csf_install_whitelist.sh - (CSF Firewall Whitelist) 

#A script that installs and tests CSF, then whitelists all appropriate IP's, I ran the script as root in the /root directory.

#msimo - 10/20/14

#A list of the IP addresses that you would like to whitelist.
ip_list=( 192.168.1.1 10.0.0.1 )

#Installs Config Server Firewall, a great plugin for iptables management and a good way to lock down your server. 
csf_install() {
	rm -fv csf.tgz
	wget http://www.configserver.com/free/csf.tgz
	tar -xzf csf.tgz
	cd csf
	sh install.sh
	csf_test
}

#Runs the csftest.pl file to see if everything checks out.
csf_test() {
	perl /usr/local/csf/bin/csftest.pl
}

#Whitelists the IP list in csf.
ip_whitelist() {
	for i in "${ip_list[@]}"
	do
		#Uncomment the below line if you are running cPanel/cPHulk.
		#/scripts/cphulkdwhitelist $i
		#echo "$i has been whitelisted on cPHulk"
		csf -a $i
		#echo "$i has been whitelisted on csf"
	done
}

#
csf_install_prompt() {
	while true; do
	    read -p "Do you wish to install csf? (y/n): " yn
	    case $yn in
	        [Yy] ) csf_install; break;;
	        [Nn] ) break;;
	        * ) echo "Please answer yes (y) or no (n).";;
	    esac
	done
}

ip_whitelist_prompt() {
	while true; do
	    read -p "Do you wish to whitelist the predetermined IP's? (y/n): " yn
	    case $yn in
	        [Yy] ) ip_whitelist; break;;
	        [Nn] ) exit;;
	        * ) echo "Please answer yes (y) or no (n).";;
	    esac
	done
}

csf_install_prompt
ip_whitelist_prompt