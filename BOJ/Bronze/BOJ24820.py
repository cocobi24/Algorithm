# https://www.acmicpc.net/problem/24820

import sys
input = sys.stdin.readline

word = list(input().rstrip())
set_word = set(word)
mid = word[0]

n = int(input())
for _ in range(n):
  s = input().rstrip()
  set_s = set(s)
  if len(set_s - set_word) == 0 and len(s) >= 4 and mid in s:
    print(s)