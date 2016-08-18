#!/bin/bash

gitRepo=""
cloneFolder=""
user="arjun"
api_key="123456789"
ip_address="127.0.0.1"
conn_string="connection string"

usage(){
	echo "***************************Usage**************************"
	echo "./q05.sh -g <github repo URL> -f <clone destination folder"
	echo "**********************************************************"
}

cloneRepo(){
	git clone $gitRepo $cloneFolder
	if [ $? -ne 0 ]
	then
		echo "Repository Cloning Failed"
		exit 1
	fi
}

formatJson(){
	if [ -e $cloneFolder/config.json ]
	then
		./q04.py -j $cloneFolder"/config.json" -u $user -a $api_key -i $ip_address -c $conn_string
		 if [ $? -ne 0 ]
        	then
                	echo "JSON parsing failed"
	                exit 1
        	fi
	fi

}

changeOwner(){
	chown -R testuser: $cloneFolder
        if [ $? -ne 0 ]
        then
                echo "Changing Permission Failed"
                exit 1
        fi

}


if [ "$#" -eq 0 ]
then
  	usage
	exit 1
else
	while [ "$1" != "" ]; do
    		case $1 in
		        -g)   	shift
				gitRepo=$1
		        	;;
		    	-f)	shift
				cloneFolder=$1
   				;;
			-h | --help )   usage
                	        exit
                        	;;
		        * )             usage
                	        exit 1
		esac
		shift
	done
fi

cloneRepo

echo $gitRepo
echo $cloneFolder
