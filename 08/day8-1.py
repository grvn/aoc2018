#!/usr/bin/env python3
from sys import argv

def main():
  with open(argv[1]) as f:
    input=[int(x) for x in next(f).split()]
  _,meta=find_meta(input, [])
  svar=sum(meta)
  print(svar)

def find_meta(input,metadata):
  cnodes,meta=input[:2]
  input=input[2:]
  if cnodes==0:
    metadata+=input[:meta]
    return(input[meta:],metadata)
  for _ in range(0, cnodes):
    input,metadata=find_meta(input,metadata)
  metadata+=input[:meta]
  return(input[meta:],metadata)

if __name__ == '__main__':
  main()
