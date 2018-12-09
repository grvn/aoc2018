#!/usr/bin/env python3
from sys import argv
from re import findall
from collections import Counter

def main():
  with open(argv[1]) as f:
    input=[[int(y) for y in findall(r'-?\d+', x)] for x in f]
  claims=[z for part in ([(claim[1] + x, claim[2] + y) for x in range(claim[3]) for y in range(claim[4])] for claim in input) for z in part]
# platta ut en lista av listor till en lista
# [ a for b in ([],[],[]) for a in b ]
  counts = Counter(claims)
  svar = len([x for x in set(claims) if counts[x] > 1])
  print(svar)

if __name__ == '__main__':
  main()
