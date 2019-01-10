#!/usr/bin/env python3
from sys import argv
from itertools import product

# byggde om majoriteten av lösningen då del1 tog timmar 
# att exekvera när den moddats för del2, förgenererar 
# värden istället för brute force

size=int(argv[2])+1 # storlek på area size x size

def main():
  with open(argv[1]) as f:
    input=next(int(x) for x in f)
  cells={(x,y): power_lvl(input,x,y) for x,y in product(range(1,size), repeat=2)} # kom ihåg denna, kan vara snabbare istället för for i for
  sumsofrows={}
  units={}
  for y in range(1,size):
    val=0
    for l,x in enumerate(range(1,size),1):
      val+=cells[(x,y)]
      sumsofrows[(l,y)]=val
  for s in range(1,size):
    for x,y in product(range(1,size+1-s), repeat=2):
      val=0
      for dy in range(s):
        val+=get_index(sumsofrows,x+s-1,y+dy) - get_index(sumsofrows,size-(size-x+1),y+dy)
      units[(x,y,s)]=val
  svar=max(units.keys(), key=(lambda key: units[key]))
  print(svar)

def get_index(d,x,y):
  if x<1 or y<1:
    return 0
  else:
    return d.get((x,y))

def power_lvl(n,x,y):
  return ((x+10)*y + n) * (x+10) // 100 % 10 - 5

if __name__ == '__main__':
  main()
