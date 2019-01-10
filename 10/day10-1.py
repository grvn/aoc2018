#!/usr/bin/env python3
from sys import argv
from re import findall

def main():
  curr_area=None
  time=0
  with open(argv[1]) as f:
    input=list(tuple(map(int, findall(r'-?\d+', x))) for x in f)
  while True:
    h=max(x+time*dx for x,_,dx,_ in input)
    v=min(x+time*dx for x,_,dx,_ in input)
    u=max(y+time*dy for _,y,_,dy in input)
    n=min(y+time*dy for _,y,_,dy in input)
    area=(h-v)*(u-n)
    if curr_area is not None and area>curr_area:
      time-=1
      break
    curr_area=area
    time+=1
  points=list()
  for x,y,dx,dy in input:
    a=x+(time*dx)-v
    b=y+(time*dy)-n
    points.append((a,b))
  for y in range(u-n):
    print(''.join('#' if (x,y) in points else ' ' for x in range(h-v)))

if __name__ == '__main__':
  main()
