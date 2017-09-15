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

# Refining /etc/hosts
ref=$(sudo cat $h | head -1 )
if [[ ! $ref == "# Refined" ]]; then
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
	echo "Refining done."
fi

if [[ $1 == "-l" ]]; then
	echo "Domains reserved/blocked :"
	touch hn
	grep "^[^#].*$" $h | cut -d" " -f 2- >> hn
	sed -i 's/\s\s*/\n/g' hn
	cat hn | sort | uniq
	rm hn
elif [[ $1 == "-u" ]]; then
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
else
	name=$1
	cp $h .
	sed -i "s/#\sIP4/# IP4\n127.0.0.1 $name/g" hosts
	sed -i "s/#\sIP6/# IP6\n::1 $name/g" hosts
	sudo mv hosts /etc
	echo "Domain blocked."
	echo "You may have to restart your browser(s)."
fi

