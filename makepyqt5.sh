#!/bin/bash

for f in *.ui
do
    filename=$(basename "$f")
    filename="${filename%.*}"
    pyuic5 -x $f -o $filename.py
done
