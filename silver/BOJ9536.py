# https://www.acmicpc.net/problem/9536

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  word = input().rstrip().split()
  word_set = set(word)
  howls = set()
  while True:
    s = input().rstrip()
    if s == "what does the fox say?":
      break
    animal, _, howl = map(str, s.split())
    howls.add(howl)
  fox = list(word_set - howls)
  print(*[w for w in word if w in fox])