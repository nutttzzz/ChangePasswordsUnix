#!/bin/bash
while [ 1 ]
do
	if [ -z $1 ] || [ -z $2 ];
	then
		echo -e "time.sh <seconds to wait> <Password length>\n60 seconds = minute\n600 seconds = 10 minutes"
		exit
	fi

sleep $1
python main.py $2
done
