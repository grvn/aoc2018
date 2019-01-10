#!/usr/bin/env python3
from sys import argv
from re import findall
from collections import deque

def main():
  with open(argv[1]) as f:
    input=[[int(y) for y in findall(r'\d+', x)] for x in f]
  players,max_marble,facit=input[0][:3] if len(input[0])>2 else input[0][:2]+[None]
  marbles=deque([0])
  score=list(0 for _ in range(players))
  for x in range(1,max_marble+1): # första poänggivande är kula 1
    if x%23:
      marbles.rotate(1)
      marbles.appendleft(x)
    else:
      marbles.rotate(-7)
      score[x%players]+=x+marbles.popleft()
      marbles.rotate(1)
  svar=max(score)
  print(svar)
  if facit:
    if facit == svar:
      print("Vilket stämmer med facitet")
    else:
      print("Stämmer ej med facit: "+str(facit))


if __name__ == '__main__':
  main()
