#!/bin/bash

if [[ ! -v AOC_SESSION ]]
then
  echo "AOC_SESSION variable is unset"
  exit 1
fi

export TZ="America/New_York"
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)

if (( $month < 12 || $day > 25 ))
then
  echo "no AoC event currently running"
  exit 1
fi

file="/home/colm/git/advent-of-code/$year/puzzle$day/input.txt"
echo "attempting to download $file"

if [[ ! -w $(dirname $file) ]]
then
  echo "cannot write to filepath"
  exit 1
fi

if [[ -f $file ]]
then
  echo "file already exists"
  exit 1
fi

url="https://adventofcode.com/$year/day/$((10#$day))/input"
curl $url --cookie "session=$AOC_SESSION" > $file

if [[ -v EDITOR ]]
then
  exec $EDITOR $file
fi
