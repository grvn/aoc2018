#!/usr/bin/env python3
from sys import argv
from itertools import cycle
from itertools import accumulate

def main():
  freq={0}
  with open(argv[1]) as f:
    print(next(x for x in accumulate(cycle(map(int, list(filter(None, (line.rstrip() for line in f)))))) if x in freq or freq.add(x)))

if __name__ == '__main__':
  main()

# mer läsbar version
# def main():
#   freq={0}
#   filename=argv[1]
#   with open(filename) as f:
#     input=list(filter(None, (line.rstrip() for line in f))) # Bli av med ev. tomma rader
#   for x in accumulate(cycle(map(int, input))):
#     if x in freq:
#       break
#     else:
#       freq.add(x)
#   print(x)
