#!/bin/bash

# Script to block specified websites
# Works with all browsers ( by exploiting /etc/hosts file )
# Currently implemented for Ubuntu

# Developed by Yash Shah

h=/etc/hosts
if [[ ! -e "$h" ]]; then
	echo "Your machine does not support this script."
	exit
fi

# Argument check
if [[ $# -eq 0 ]]; then
	echo "Invalid usage."
	echo "Type ' ./block.sh -h ' for help."
	exit
fi

# Help menu
if [[ $1 == "-h" || $1 == "--help" ]]; then
	echo "Usage: ./block.sh [domain_names separated by <space>]"
	echo -e "\tBlocks the specified domain name(s)"
	echo -e "Usage: ./block.sh [ -h,--help | -u,--unblock [domain_name(s)] | -l,--list |\n\t\t    -r,--reset ]"
	echo -e "\t-h,--help\tDisplays this help and exits"
	echo -e "\t-u,--unblock\tUnblocks the specified domain name(s)\n\t\t\tseparated by <space>"
	echo -e "\t-l,--list\tDisplays all the existing reserved/blocked domains"
	echo -e "\t-r,--reset-soft\tResets file to 'refined' configuration"
	echo -e "\t-R,--reset-hard\tResets file to original"
	exit	
fi

# Refining /etc/hosts
ref=$(sudo cat $h | head -1 )
if [[ ! $ref == "# Refined" ]]; then
	sudo cp $h /etc/hosts_org
	echo "Refining $h..."
	touch hosts
	f=hosts
	chmod 755 $f
	echo "# Refined" >> $f
	echo "" >> $f
	echo "# IP4" >> $f
	grep "\." $h | awk '{print $0}' >> $f
	echo "" >> $f
	echo "# IP6" >> $f
	grep "::" $h | awk '{print $0}' >> $f
	sed -i -e 's/\t\t*/ /g' -e 's/\s\s*/ /g' $f
	sudo mv $f /etc/ # this will overwrite the file
	sudo cp $h /etc/hosts_ref
	echo "Refining done."
fi

if [[ $1 == "-l" || $1 == "--list" ]]; then
	echo "Domains reserved/blocked :"
	touch hn
	grep "^[^#].*$" $h | cut -d" " -f 2- >> hn
	sed -i 's/\s\s*/\n/g' hn
	cat hn | sort | uniq
	rm hn
elif [[ $1 == "-u" || $1 == "--unblock" ]]; then
	if [[ $# -eq 2 ]]; then
		if [[ $(grep "\s$2\s*$" $h) == "" ]]; then
			echo "Domain not found."
			echo "Try ' ./block.sh -l ' for a list of reserved/blocked domains."
		else
			if [[ $2 =~ ip6-.* ]]; then
				echo "Reserved domain. Cannot modify."
				exit
			elif [[ $2 == "localhost" || $2 == $(hostname) ]]; then
				echo "Reserved domain. Cannot modify."
				exit
			fi
			
			cp $h .
			sed -i "/\s$2\s*$/d" hosts
			sudo mv hosts /etc
			echo "'$2' unblocked."
		fi
	elif [[ $# -gt 2 ]]; then
		cp $h .
		for name in ${@:2}
		do
			if [[ $(grep "\s$name\s*$" $h) == "" ]]; then
				echo "Domain '$name' not found."
			else
				if [[ $name =~ ip6-.* || $name == "localhost" || $name == $(hostname) ]]; then
					echo "'$name' is reserved. Cannot modify."
				else
					sed -i "/\s$name\s*$/d" hosts
				fi
			fi
		done
		sudo mv hosts /etc
		echo "Domains unblocked."
	fi
elif [[ $1 == "-r" || $1 == "--reset-soft" ]]; then
	sudo cp /etc/hosts_ref $h # this overwrites existing file
	echo "File reset to refined configuration."
	exit

elif [[ $1 == "-R" || $1 == "--reset-hard" ]]; then
	sudo cp /etc/hosts_org $h # this overwrites existing file
	sudo rm /etc/hosts_org /etc/hosts_ref
	echo "File reset to original."
	exit

else
	if [[ $# -gt 1 ]]; then
		cp $h .
		for name in $@
		do
			sed -i "s/#\sIP4/# IP4\n127.0.0.1 $name/g" hosts
			sed -i "s/#\sIP6/# IP6\n::1 $name/g" hosts
		done
		sudo mv hosts /etc
		echo "Domains blocked."
		echo "You may have to restart your browser(s)."
	else
		cp $h .
		sed -i "s/#\sIP4/# IP4\n127.0.0.1 $1/g" hosts
		sed -i "s/#\sIP6/# IP6\n::1 $1/g" hosts
		sudo mv hosts /etc
		echo "Domain blocked."
		echo "You may have to restart your browser(s)."
	fi
fi

