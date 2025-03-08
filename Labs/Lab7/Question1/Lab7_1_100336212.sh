#!/bin/bash 
read -p "Which server should be pinged: " server_addr 
 
# -c 1 sends 1 echo request 
# -4 means IPv4 , -6 IPv6 or ping6 
# 2 (standard error) > err (any file) 
# || only executes the second if the previous fails 
 
ping -4 -c 2 $server_addr 2>err || echo "Server Dead"