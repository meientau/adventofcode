#!/bin/bash
s=0;m=0;while read n;do if [ -z "$n" ]; then [ $s -gt $m ]&&m=$s;s=0;fi;s=$((s+n));done<input;echo $m
