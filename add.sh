#!/bin/bash

git status | grep modified |
while read file
do
    fil=$( echo $file | xargs | cut -d " " -f2)
    echo "adding ${fil}"
    git add "$fil"
done
