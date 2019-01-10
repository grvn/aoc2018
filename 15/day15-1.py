#!/usr/bin/env python3
from sys import argv
from heapq import heappop
from heapq import heappush

#########################################
# Denna innehåller problem med hörnfall #
# påverkar ej resultatet av input       #
# dessa är fixade i day15-2.py          #
# har ej orkat fixa dem här             #
#########################################

atp=3
starthp=200

def main():
  elves={}
  goblins={}
  walls=set()
  turns=0
  with open(argv[1]) as f:
    input=[list(x.strip()) for x in f]
  for y,line in enumerate(input):
    for x,val in enumerate(line):
      if val=='E':
        elves[(x,y)]=starthp
      elif val=='G':
        goblins[(x,y)]=starthp
      elif val=='#':
        walls.add((x,y))

  while elves and goblins:
    order=sorted(list(elves)+list(goblins),key=lambda x:(x[1],x[0]))
    while order:
      # order är sorterad efter ordningen de får röra sig
      who=order.pop(0)
      if who in elves: # det är en elf
        hp=elves.pop(who)
        notfoos=elves
        foos=goblins
      elif who in goblins: # det är en goblin
        hp=goblins.pop(who)
        notfoos=goblins
        foos=elves
      else: # död innan den får agera
        continue
      targets=list(foos)
      inuse=set(elves)|set(goblins)|walls
      inrange=adjacent(targets)-inuse
      nextmove=pickmove(who,inrange,inuse)
      if nextmove is None: # kan inte göra något
        notfoos[who]=hp
        continue
      notfoos[nextmove]=hp
      if nextmove in inrange: # kan attackera
        attack(nextmove,foos)
    if elves and goblins:
      turns+=1
  print(turns*(sum(elves.values())+sum(goblins.values())))

def attack(mypos,targets):
  inrange=adjacent({mypos})
  postargets=[x for x in inrange if x in targets]
  if postargets:
    target=min(postargets, key=lambda x: targets[x])
    targets[target]-=atp
    if targets[target]<=0:
      targets.pop(target)

def adjacent(positions):
  return set ((x+dx,y+dy) for x,y in positions for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)])

def pickmove(mypos,targetpos,inuse):
  if not targetpos: # finns inga rutor bredvid mål som går att nå
    return None
  if mypos in targetpos:
    return mypos
  routes=shortestroutes(mypos,targetpos,inuse)
  posmove=[x[1] for x in routes]
  return min(posmove,key=lambda x:(x[1],x[0])) if posmove else None

def shortestroutes(mypos,targetpos,inuse): # tack google Dijkstra's algoritm
# heapq har ingen sortfunction som man kan skicka lambda till!
# måste invertera x,y för att få sort korrekt
# borde ha haft koordinater som (y,x) från början
# eller söka vidare på google efter prioriterad kö
  res=[]
  shortest=None
  been=set([t[::-1] for t in inuse])
  x,y=mypos
  todo=[(0,[(y,x)])]
  tarpos=[t[::-1] for t in targetpos]
  while todo:
    dist,path=heappop(todo)
    if shortest and len(path)>shortest: # se om vi funnit kortast och gått längre
      return res
    currpos=path[-1] # ta sista objekt
    if currpos in tarpos: # funnit kortast väg
      res.append([t[::-1] for t in path])
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
