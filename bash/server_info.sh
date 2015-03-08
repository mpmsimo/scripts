#!/usr/bin/bash
#server_info.sh - Gets system information of a linux machine.
#Tested with CentOS 6.6 x64
#msimo - 3/8/15

print_title() {
	awk 'BEGIN {while (c++<80) printf "#"}'
	echo -e "\n                    "$1 
	awk 'BEGIN {while (c++<80) printf "#"}'
	echo
}

clear # Clears the terminal so this beautiful program can be seen.

#echo "This  is `uname -s` running on a `-uname -m` processor."
print_title "Operating System (Distro, Kernel, Arch, Bit)"
#cat /etc/*-release
#lsb_release -a
cat /proc/version

print_title "CPU information"
#cat /proc/cpuinfo

print_title "Memory Usage"
free -m

print_title "Partitions and hardrive capacity"
df -ah --total # Showing the partitions as well as the total capacity of the harddrives.

print_title "Network Settings"
#ifconfig

print_title "Gateway"
#route -n # look for gateway associated with the UG flag

print_title "Uptime"
uptime

print_title "Users logged on"
who
#finger
