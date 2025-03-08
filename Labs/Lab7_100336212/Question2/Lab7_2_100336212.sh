#!/bin/bash 
 
read -p "Enter the username: " username 
sudo useradd $username 

echo -n "The home directory: " && ls -l ~/.. | grep $username #could also be done in awk, but awk doesn't enjoy external variables
 
# -e to be able to execute \n 
echo -e "\n Change the password" 
sudo passwd $username 
 
echo -e "\n Test your new user account" 
sudo su ${username} 
 
# sudo userdel -r username (to delete the account) 