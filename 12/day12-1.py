#!/usr/bin/env python3
from sys import argv
from collections import defaultdict

def main():
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  state=defaultdict(lambda: '.', {n:x for n,x in enumerate(input[0].split(': ')[1])}) # defaultdict för att få adresser utanför 0->längd av state att fungera utan massa onödig felhantering
  input=dict(x.split(' => ') for x in input[2:])
  for x in range(1, 21):
    tmp={}
    val=[]
    for p in range(min(state)-2, max(state)+2):
      val=[] # töm den
      for y in range(p-2,p+3):
        val.append(state[y])
      tmp[p]=input[''.join(val)]
    state=defaultdict(lambda: '.', tmp)
  svar = sum(x for x in state if state[x]=='#')
  print(svar)

if __name__ == '__main__':
  main()
