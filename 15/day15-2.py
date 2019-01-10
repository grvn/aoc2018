#!/usr/bin/env python3
from sys import argv
from heapq import heappop
from heapq import heappush

starthp=200

#####################################################
# Hela kartan är inverterad så istället för x,y i   #
# 15-1 så är det nu y,x                             #
# fick inte selektionen att fungera i hörnfall med  #
# prioriterad queue utan att först göra invertering #
#####################################################

def main():
  elves={}
  goblins={}
  walls=set()
  with open(argv[1]) as f:
    input=[list(x.strip()) for x in f]
  for y,line in enumerate(input):
    for x,val in enumerate(line):
      if val=='E':
        elves[(y,x)]=starthp
      elif val=='G':
        goblins[(y,x)]=starthp
      elif val=='#':
        walls.add((y,x))
  needtosurvive=len(elves)
#  elves={(5, 24): 200, (6, 23): 77, (8, 22): 176, (9, 21): 122, (9, 24): 134, (11, 21): 35, (12, 20): 140, (12, 23): 200, (21, 15): 131, (22, 14): 140} # kopplad till test35
#  goblins={(4, 23): 200, (5, 23): 96, (6, 22): 200, (7, 19): 200, (8, 21): 5, (9, 20): 200, (10, 21): 200, (11, 20): 31, (21, 14): 31, (22, 13): 200} # kopplad till test35

  elfpower=4
#  elfpower=13 # kopplad till test35
  while True:
    saveelf=elves.copy()
    savegoblin=goblins.copy()
    turns=0
    while elves and goblins:
      order=sorted(list(elves)+list(goblins))
      while order:
        # order är sorterad efter ordningen de får röra sig
        who=order.pop(0)
        if who in elves:
          hp=elves.pop(who)
          notfoos=elves
          foos=goblins
          atp=elfpower
          # det är en elf
        elif who in goblins:
          hp=goblins.pop(who)
          notfoos=goblins
          foos=elves
          atp=3
          # det är en goblin
        else: # död
          continue
        targets=list(foos)
        inuse=set(elves)|set(goblins)|walls
        inrange=adjacent(targets)-inuse
        nextmove=pickmove(who,inrange,inuse)
        if nextmove is None: # Kan inte göra något
          notfoos[who]=hp
          continue
        notfoos[nextmove]=hp
        if nextmove in inrange: # kan attackera efter förflyttningen
          attack(nextmove,foos,atp)
      if elves and goblins:
        turns+=1
    if needtosurvive==len(elves):
      break
    elfpower+=1
#    exit()
    elves=saveelf.copy()
    goblins=savegoblin.copy()
  print(turns*(sum(elves.values())+sum(goblins.values())))

def attack(mypos,targets,atp):
  inrange=adjacent({mypos})
  postargets=[x for x in inrange if x in targets]
  if postargets:
#    print(postargets)
    target=min(postargets, key=lambda x: (targets[x],x[0]))
    targets[target]-=atp
    if targets[target]<=0:
      targets.pop(target)

def adjacent(positions):
  return set ((y+dy,x+dx) for y,x in positions for dy,dx in [(0,-1),(-1,0),(0,1),(1,0)])

def pickmove(mypos,targetpos,inuse):
  if not targetpos: # finns inga rutor bredvid mål som går att nå
    return None
  if mypos in targetpos: #behöver ej röra sig
    return mypos
  routes=shortestroutes(mypos,targetpos,inuse) #hitta närmanste väg
  posmove=[x[1] for x in routes] # få första steg på varje väg
  return min(posmove) if posmove else None

def shortestroutes(mypos,targetpos,inuse):
  res=[]
  shortest=None
  been=set(inuse)
  todo=[(0,[mypos])]
  while todo:
    dist,path=heappop(todo)
    if shortest and len(path)>shortest: # se om vi funnit kortast och gått längre
      return res
    currpos=path[-1] # ta sista objekt
    if currpos in targetpos: # funnit kortast väg
      res.append(path)
      shortest=len(path)
      continue
    if currpos in been: # redan besökt
      continue
    been.add(currpos)
    for neigh in adjacent({currpos}):
      if neigh in been:
        continue
      heappush(todo,(dist+1,path+[neigh]))
  return res

if __name__ == '__main__':
  main()
