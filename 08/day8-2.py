#!/usr/bin/env python3
from sys import argv

def main():
  with open(argv[1]) as f:
    input=[int(x) for x in next(f).split()]
  _,_,svar=find_meta(input, [])
  print(svar)

def find_meta(input,metadata):
  children={}
  cnodes,meta=input[:2]
  input=input[2:]
  if cnodes==0:
    return(input[meta:],input[:meta],sum(input[:meta]))
  for x in range(1, cnodes+1): # offset 1 p.g.a. uppgiften indexerar barn 1..n
    input,_,children[x]=find_meta(input,metadata)
  metadata=input[:meta]
  total=sum(children[m] for m in metadata if m in children)
  return(input[meta:],metadata,total)

if __name__ == '__main__':
  main()
