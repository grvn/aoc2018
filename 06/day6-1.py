#!/usr/bin/env python3
from sys import argv
from functools import reduce
from collections import Counter

def main():
  with open(argv[1]) as f:
    input=list(tuple(map(int,x.split(', '))) for x in f)
# Ta reda på arbetsytan, utanför=inf
# v=vänster, u=upp, h=höger, n=ned
  v,u=reduce(lambda x,y: map(min, zip(x,y)), input)
  h,n=reduce(lambda x,y: map(max, zip(x,y)), input)
  karta={}
  for x in range(v,h+1):
    for y in range(u,n+1):
      min_dist=None
      nearest=None
      for p in input:
        dist=manhattan_distance(p,(x,y))
        if min_dist is None or dist < min_dist:
          nearest=p
          min_dist=dist
        elif dist==min_dist:
          nearest=None
      if nearest is not None:
        karta[x,y]=nearest
# närmast kanten = inf
  infinite={(a,b) for ((x,y),(a,b)) in karta.items() if x in {v,h} or y in {u,n}}
  c=Counter((a,b) for ((x,y),(a,b)) in karta.items() if (a,b) not in infinite)
  svar=c.most_common(1)[0][1]
  print(svar)

def manhattan_distance(x,y):
  (ax,ay)=x
  (bx,by)=y
  return abs(ax-bx)+abs(ay-by)

if __name__ == '__main__':
  main()
