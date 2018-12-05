#!/usr/bin/env python3
from sys import argv

def main():
  x=1
  with open(argv[1]) as f:
    input=list(f.read().strip())
  while True:
    if input[x-1]==input[x].swapcase():
      del input[x-1:x+1]
      x-=1 if x>1 else 0
    else:
      x+=1
    if x>=len(input):
      break

  print(len(input))

if __name__ == '__main__':
  main()
