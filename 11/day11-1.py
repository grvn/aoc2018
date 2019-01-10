#!/usr/bin/env python3
from sys import argv

size=int(argv[2]) # storlek på area size x size, för testning
box_size=3

def main():
  with open(argv[1]) as f:
    input=next(int(x) for x in f)
  cells={(x,y): power_lvl(input,x,y) for x in range(1,size+1) for y in range(1,size+1)}
  units={(x,y): sum((get_power(cells,x+i,y+j)) for j in range(box_size) for i in range(box_size)) for x in range(1,size+2-box_size) for y in range(1,size+2-box_size)}
  svar=max(units.keys(), key=(lambda key: units[key]))
  print(svar)

def get_power(cells,x,y):
  if x<1 or x>size or y<1 or y>size:
    return 0
  return cells[(x,y)]

def power_lvl(n,x,y):
  return ((x+10)*y + n) * (x+10) // 100 % 10 - 5

def test_power_lvl():
  print(power_lvl(57,122,79)) # bör ge -5
  print(power_lvl(39,217,196)) # bör ge 0
  print(power_lvl(71,101,153)) # bör ge 4

if __name__ == '__main__':
  main()
