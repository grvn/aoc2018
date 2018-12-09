#!/usr/bin/env python3
from sys import argv
from re import findall
from collections import Counter

def main():
  with open(argv[1]) as f:
    input=[[int(y) for y in findall(r'-?\d+', x)] for x in f]
  idclaims={claim[0]: [(claim[1] + x, claim[2] + y) for x in range(claim[3]) for y in range(claim[4])] for claim in input}
  claims=[z for part in idclaims.values() for z in part] # platta ut en lista av listor till en lista
  counts = Counter(claims)
  problems = [x for x in set(claims) if counts[x] > 1]
  svar = next(x for x in idclaims if not set(idclaims[x]) & set(problems))
  print(svar)

if __name__ == '__main__':
  main()
