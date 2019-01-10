#!/usr/bin/env python3
from sys import argv

def main():
  recept='37'
  e1=0 # index 0 i strängen recept
  e2=1 # index 1 i strängen recept
  with open(argv[1]) as f:
    input=next(int(x) for x in f)
  while len(recept)<input+10:
    recept+=str(int(recept[e1])+int(recept[e2]))
    e1=(e1+int(recept[e1])+1)%len(recept)
    e2=(e2+int(recept[e2])+1)%len(recept)
  svar=recept[-10:]
  print(svar)

if __name__ == '__main__':
  main()
