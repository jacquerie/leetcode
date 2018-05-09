#!/usr/bin/env bash

tr -s " " "\n" <words.txt | sort | uniq -c | sort -n -r | awk -F ' ' '{ print $2 " " $1 }'
