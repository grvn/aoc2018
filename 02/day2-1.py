#!/usr/bin/env python3
from sys import argv
from collections import Counter

def main():
  two=0
  three=0
  with open(argv[1]) as f:
    for row in f:
      c=Counter(list(row))
      if 2 in c.values():
        two+=1
      if 3 in c.values():
        three+=1
  print(two*three)

if __name__ == '__main__':
  main()
