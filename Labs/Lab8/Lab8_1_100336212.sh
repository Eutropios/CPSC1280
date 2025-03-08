#!/bin/bash

fileToRead=$1
read -p "Enter the pattern you are searching for: " pattern

grep "$pattern" $fileToRead | awk '{print($0); lines +=1} END{print("Number of lines: ", lines)}'