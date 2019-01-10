#!/usr/bin/env python3
from sys import argv

cart={'^','>','v','<'}
headings={'^': lambda x,y: (x,y-1), '>': lambda x,y: (x+1,y), 'v': lambda x,y: (x,y+1), '<': lambda x,y: (x-1,y)}
turn={'^':{'/':'>','\\':'<'},'>':{'/':'^','\\':'v'},'v':{'/':'<','\\':'>'},'<':{'/':'v','\\':'^'}}
cross={'^': lambda val:('<','^','>')[val],'>': lambda val:('^','>','v')[val],'v': lambda val:('>','v','<')[val],'<': lambda val:('v','<','^')[val]}

def main():
  with open(argv[1]) as f:
    input = [line.strip('\n') for line in f]
  tracks = {(int(x), int(y)): s for y,r in enumerate(input) for x,s in enumerate(r) if s!=' '}
  carts = {x: (tracks[x],0) for x in tracks if tracks[x] in cart}
  num_carts=len(carts)
  for x in carts:
    tracks[x] = '|' if tracks[x] in {'^','v'} else '-'
  crash=False
  while not crash:
    new_pos={}
    for a in carts:
      x,y=a
      next_coord=headings[carts[a][0]](x,y)
      if next_coord in new_pos:
        crash=True
        break
      tnc=tracks[next_coord]
      if tnc in {'/','\\','+'}:
        if tnc in {'/','\\'}:
          new_pos[next_coord]=(turn[carts[a][0]][tnc],carts[a][1])
        elif tnc=='+':
          val=carts[a][1]
          new_val=(val+1)%3
          new_pos[next_coord]=(cross[carts[a][0]](val),new_val)
      else:
        new_pos[next_coord]=carts[a]
    carts=new_pos
  svar=(next_coord)
  print(svar)

if __name__ == '__main__':
  main()
