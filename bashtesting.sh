#!/bin/bash
files=$(<files.txt)

for file in "${files[@]}"; do 
    git reset $file
done