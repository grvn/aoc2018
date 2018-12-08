#!/usr/bin/env python3
from sys import argv
from re import findall
from collections import defaultdict

def main():
  guards=defaultdict(lambda: [0 for x in range(60)])
  guard=[False,None,None] # sover, id, minut somna
  with open(argv[1]) as f:
    input = [[int(y) for y in findall(r'\d+', x)] for x in sorted(f, key=lambda y: y[1:17])]
  for x in input:
    if len(x) == 6: # ny vakt
      guard[1]=x[5]
    else:
      if guard[0]: # vakna
        sub=guards[guard[1]][guard[2]:x[4]]
        sub=[x+1 for x in sub]
        guards[guard[1]][guard[2]:x[4]]=sub
      else: # somna
        guard[2] = x[4]
      guard[0] = not guard[0]
  summed={k: sum(v) for (k, v) in guards.items()} # hitta total sovtid per vakt
  sleeper=max(summed, key=lambda key: summed[key]) # hitta den vakt med högst total sovtid
  time=guards[sleeper].index(max(guards[sleeper])) # beräkna hur länge vakt funnen tidigare sov som längst
  print(sleeper*time)

if __name__ == '__main__':
  main()
