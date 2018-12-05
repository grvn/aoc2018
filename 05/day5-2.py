#!/usr/bin/env python3
from sys import argv

def main():
  with open(argv[1]) as f:
    input=list(f.read().strip())
  test=set(map(lambda y:y.lower(),input))
  svar=len(input)
  for z in test:
    svar = min(svar,part1([a for a in input if a.casefold() != z]))
  print(svar)

def part1(input):
  x=1
  while True:
    if input[x-1]==input[x].swapcase():
      del input[x-1:x+1]
      x-=1 if x>1 else 0
    else:
      x+=1
    if x>=len(input):
      break
  return len(input)

if __name__ == '__main__':
  main()
