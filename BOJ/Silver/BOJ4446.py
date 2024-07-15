# https://www.acmicpc.net/problem/4446

import sys
input = sys.stdin
vowels = ['a', 'i', 'y', 'e', 'o', 'u', 'a', 'i', 'y']
VOWELS = [v.upper() for v in vowels]

consonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f', 'b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g']
CONSONANT = [c.upper() for c in consonant]

while True:
  message = input.readline()
  if not message:
    break
  message = list(message.rstrip())
  ROT13 = ""
  for m in message:
    if m.islower():
      if m in vowels:
        m = vowels[vowels.index(m) + 3]
      else:
        m = consonant[consonant.index(m) + 10]
    elif m.isupper():
      if m in VOWELS:
        m = VOWELS[VOWELS.index(m) + 3]
      else:
        m = CONSONANT[CONSONANT.index(m) + 10]
    ROT13 += m
  print(ROT13)