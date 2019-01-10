#!/usr/bin/env python3
from sys import argv
from collections import defaultdict
from collections import deque

generations=50000000000
old_total=deque(maxlen=100) # anta att om antalet ökar konstant 100 ggr. så fortsätter den med det

def main():
  with open(argv[1]) as f:
    input = [line.strip() for line in f]
  state=defaultdict(lambda: '.', {n:x for n,x in enumerate(input[0].split(': ')[1])})
  input=dict(x.split(' => ') for x in input[2:])
  diff=0
  for x in range(1, generations+1):
    tmp={}
    val=[]
    for p in range(min(state)-2,max(state)+2):
      val=[]
      for y in range(p-2,p+3):
        val.append(state[y])
      tmp[p]=input[''.join(val)]
    state=defaultdict(lambda: '.', tmp)
    svar = sum(x for x in state if state[x]=='#')
    old_total.append(svar-diff)
    if len(old_total)==old_total.maxlen and old_total.count(old_total[0])==len(old_total):
      break
    diff=svar
  svar+=(generations-x)*old_total[0] # utifrån antagandet att det ökar konstant, beräkna totalsumman
  print(svar)

if __name__ == '__main__':
  main()
