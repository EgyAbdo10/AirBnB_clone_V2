#!/usr/bin/env bash

if [ "$2" -eq 2 ]; then
    scp -i ~/.ssh/school "$1" ubuntu@34.207.58.33:~
fi

if [ "$2" -eq 1 ]; then
    scp -i ~/.ssh/school "$1" ubuntu@100.25.144.102:~
fi

if [ "$2" -eq 12 ]; then
    scp -i ~/.ssh/school "$1" ubuntu@100.25.144.102:~
    scp -i ~/.ssh/school "$1" ubuntu@34.207.58.33:~
fi