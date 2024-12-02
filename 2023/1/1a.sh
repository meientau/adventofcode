#!/bin/bash

tr -d 'a-z' < input | sed 's/^[0-9]$/\0\0/' | sed -E 's/^([0-9]).*([0-9]).*/\1\2/' | tr '\n' '+' | sed 's/+$/\n/' | bc