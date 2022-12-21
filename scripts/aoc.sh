#!/bin/bash

#TODO add demo flag (maybe this makes more sense as a python script)
YEAR=$1
DAY=$2
PART=$3

if [ -z "$YEAR" ] || [ -z "$DAY" ] || [ -z "$PART" ]
then
echo "Usage: aoc.sh <year> <day> <part>"
exit 1
fi

if [ "$DAY" -le 9 ];
then
DAY=0$DAY
fi

#TODO set location of each repo as env var
python3 ${HOME}/Develop/aoc/${YEAR}/${DAY}/${DAY}_${PART}.py ${HOME}/Develop/aoc-input/${YEAR}/${DAY}/input_${DAY}.txt
