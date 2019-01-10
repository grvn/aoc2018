#!/usr/bin/env python3
from sys import argv
from re import compile
from re import findall

def main():
  pattern = compile('-?\d+')
  opcodes=[addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
  with open(argv[1]) as f:
    input=f.read().strip().split('\n\n\n')
  samples=input[0].split('\n\n')
  samples=[s.split('\n') for s in samples]
  samples=[[list(map(int,findall(pattern,x))) for x in s] for s in samples]
  examples=input[1].strip().split('\n')
  examples=[list(map(int,findall(pattern,x))) for x in examples]

# Hitta vilken kod som tillhör vilken instruktion
  done=False
  foundops={}
  while opcodes:
    realops={opcode:set() for opcode in opcodes}
    for s in [s for s in samples if s[1][0] not in foundops]:
      for opcode in opcodes:
        if opcode(s[0],s[1][1],s[1][2],s[1][3])==s[2][s[1][3]]:
          realops[opcode].add(s[1][0])
    for opcode in realops:
      if len(realops[opcode])==1:
        foundops[realops[opcode].pop()]=opcode
        opcodes.remove(opcode)

# Kör testprogrammet
  registers = [0,0,0,0]
  for op,a,b,c in examples:
    registers[c] = foundops[op](registers,a,b,c)
  svar=registers[0]

  print(svar)


# Operations
# Borde gjort dessa så de faktiskt manupulerar registret, 
# istället för att returnera svar och ändra dem vid returen.
# Lat på del 1
def addr(r,a,b,c):
  return r[a]+r[b]
    
def addi(registers,a,b,c):
  return registers[a]+b

def mulr(registers,a,b,c):
  return registers[a]*registers[b]

def muli(registers,a,b,c):
  return registers[a]*b

def banr(registers,a,b,c):
  return registers[a]&registers[b]

def bani(registers,a,b,c):
  return registers[a]&b

def borr(registers,a,b,c):
  return registers[a]|registers[b]

def bori(registers,a,b,c):
  return registers[a]|b

def setr(registers,a,b,c):
  return registers[a]

def seti(registers,a,b,c):
  return a

def gtir(registers,a,b,c):
  return 1 if a>registers[b] else 0

def gtri(registers,a,b,c):
  return 1 if registers[a]>b else 0

def gtrr(registers,a,b,c):
  return 1 if registers[a]>registers[b] else 0

def eqir(registers,a,b,c):
  return 1 if a==registers[b] else 0

def eqri(registers,a,b,c):
  return 1 if registers[a]==b else 0

def eqrr(registers,a,b,c):
  return 1 if registers[a]==registers[b] else 0

if __name__ == '__main__':
  main()
