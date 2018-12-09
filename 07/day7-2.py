#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def main():
  char_offset=65 # ASCII A=65, vill ha A=1
  min_work_time=int(argv[2])-char_offset
  number_of_elves=int(argv[3])
  with open(argv[1]) as f:
    input=list((x[5:6],x[36:37]) for x in f)
  prereq=defaultdict(set)
  depending=defaultdict(set)
  for x,y in input:
    depending[x].add(y)
    prereq[y].add(x)
  usable=depending.keys()-prereq.keys()
  done={}
  svar=-1 # itereringen går från nollte sekunden, fulhack för att fixa det
  elves=list((None,0) for x in range(number_of_elves)) # (bokstav, tid)
  while len(usable)>0 or not all(x[0] is None for x in elves):
    svar+=1
    for elv in elves: # uppdatera alla elves
      if elv[0] is not None:
        if elv[1] > 0:
          elves[elves.index(elv)] = (elv[0],elv[1]-1)
        else:
          elves[elves.index(elv)] = (None,0)
          usable |= depending[elv[0]]
          done[elv[0]]=None

    while len(usable)>0: # finns jobb, försök hitta en elv som inte jobbar
      try:
        elv=elves.index((None,0))
        nvalues = sorted(list(x for x in usable if all(y in done for y in prereq[x])))
        nvalue = nvalues[0]
        if elv is not None:
          tid=min_work_time+ord(nvalue)
          elves[elv]=(nvalue,tid)
          usable.remove(nvalue)
        else:
          break
      except (ValueError, IndexError): # lat, borde gå att fixa utan att ignorera errors
        break

  print(svar)

if __name__ == '__main__':
  main()
