#!/usr/bin/env python3
from sys import argv

def main():
  recept='37'
  e1=0
  e2=1
  with open(argv[1]) as f:
    input=next(x.strip() for x in f)
  while input not in recept[-len(input)-1:]:
    recept+=str(int(recept[e1])+int(recept[e2]))
    e1=(e1+int(recept[e1])+1)%len(recept)
    e2=(e2+int(recept[e2])+1)%len(recept)
  svar=recept.index(input)
  print(svar)

if __name__ == '__main__':
  main()
