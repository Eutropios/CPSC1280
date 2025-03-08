#!/bin/bash 
read -p "What is the name of the data source? (Please include the file extension): " dataSource

#numLines=`cat $dataSource | wc -l`
#awk -f corruptionComparison $dataSource

sortedByCorruption=`sort -n -t ',' -k 7 -r $dataSource | awk -F, 'NR > 1{print($0)}'`
echo ${sortedByCorruption[1]}
echo ${sortedByCorruption[2]}
echo ${sortedByCorruption[3]}


#I tried a million different things, but couldn't get anything to work. I should retake this course