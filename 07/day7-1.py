#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def main():
  with open(argv[1]) as f:
    input=list((x[5:6],x[36:37]) for x in f)
  prereq=defaultdict(set)
  depending=defaultdict(set)
  for x,y in input:
    depending[x].add(y)
    prereq[y].add(x)
  usable=depending.keys()-prereq.keys() # lista med bokstäver som kan exekveras
  svar={}
  while len(usable)>0:
    nvalues = sorted(list(x for x in usable if all(y in svar for y in prereq[x])))
    nvalue = nvalues[0]
    svar[nvalue] = None
    usable |= depending[nvalue] # slå ihop två listor
    usable.remove(nvalue)
  print(''.join(svar))

if __name__ == '__main__':
  main()
