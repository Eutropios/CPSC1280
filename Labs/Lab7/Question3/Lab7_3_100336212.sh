#!/bin/bash


Line=`ifconfig eth0 | awk 'BEGIN{FS=" "} /broadcast/{printf "%s\n", "IP address of this machine: " $2 "\n" $3 ": " $4 "\n" $5 ": " $6}'`
echo -e ${Line}