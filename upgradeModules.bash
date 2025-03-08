#!/usr/bin/bash

pip list --outdated > outdatedModules.txt
$numLines=`wc -l < outdatedModules.txt`
for i in numLines:
    echo 