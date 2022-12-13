#!/bin/bash
tr '\n' '+' < input_small | sed 's/++/\n/g'|bc|sort -nr|head -1
