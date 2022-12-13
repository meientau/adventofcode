#!/bin/bash

sed -E "s/$(for i in {1..9} ; do echo -n '.(.)..' ; done ; echo -n '?')/$(for i in {1..9} ; do echo -n "crate $i '\\$i' ;" ; done)/ ; " $1 > .input

cat .input
