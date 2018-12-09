#!/usr/bin/env python3
from sys import argv
from functools import reduce

def main():
  safeareasize=int(argv[2])
  with open(argv[1]) as f:
    input=list(tuple(map(int,x.split(', '))) for x in f)
# Ta reda på arbetsytan, utanför=inf
# v=vänster, u=upp, h=höger, n=ned
  v,u=reduce(lambda x,y: map(min, zip(x,y)), input)
  h,n=reduce(lambda x,y: map(max, zip(x,y)), input)
  svar=0
  karta={}
  for x in range(v,h+1):
    for y in range(u,n+1):
      min_dist=None
      nearest=None
      total_dist=0
      for p in input:
        dist=manhattan_distance(p,(x,y))
        total_dist+=dist
        if min_dist is None or dist < min_dist:
          nearest=p
          min_dist=dist
        elif dist==min_dist:
          nearest=None
      if nearest is not None:
        karta[x,y]=nearest
      if total_dist < safeareasize:
        svar+=1
  print(svar)

def manhattan_distance(x,y):
  (ax,ay)=x
  (bx,by)=y
  return abs(ax-bx)+abs(ay-by)

if __name__ == '__main__':
  main()
