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
  carts = {(0,*x): (tracks[x],0) for x in tracks if tracks[x] in cart}
  num_carts=len(carts)
  for _,x,y in carts:
    tracks[(x,y)] = '|' if tracks[(x,y)] in {'^','v'} else '-'

  while True:
    time,x,y=min(carts)
    direction,selection=carts.pop((time,x,y))
    next_coord=headings[direction](x,y)
    if len(carts)==0: # kom ihåg att den rör sig ett steg efter sista krasch INNAN svaret är korrekt!
      svar=(next_coord)
      break
    tnc=tracks[next_coord]
    if tnc in {'/','\\','+'}:
      if tnc in {'/','\\'}:
        direction=turn[direction][tnc]
      elif tnc=='+':
        direction=cross[direction](selection)
        selection=(selection+1)%3
    if (time,*next_coord) in carts:
      carts.pop((time,*next_coord))
    elif (time+1,*next_coord) in carts:
      carts.pop((time+1,*next_coord))
    else:
      carts[(time+1,*next_coord)]=(direction,selection)
  print(svar)

if __name__ == '__main__':
  main()
