#!/usr/bin/env python3
from sys import argv

def main():
  with open(argv[1]) as f:
    input=f.readlines()
  id1,id2=next((x,y) for x in input for y in input if sum(1 for a,b in zip(x,y) if a!=b)==1) # Hitta de två rätta ID där endast ett enda tecken diffar
  svar="".join(x for x,y in zip(id1,id2) if x==y).strip() # jämför de två rätta och ta bort de tecken som inte stämmer
  print(svar)

if __name__ == '__main__':
  main()
