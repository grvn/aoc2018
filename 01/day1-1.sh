#!/bin/bash
s=0;while read -r l; do (( s += l )); done < $1; echo $s
