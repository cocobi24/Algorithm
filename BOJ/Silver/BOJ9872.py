# https://www.acmicpc.net/problem/9872

import sys
input = sys.stdin.readline

n = int(input())
note = {}
for _ in range(n):
  group = tuple(sorted(input().rstrip().split()))
  if group in note:
    note[group] += 1
  else:
    note[group] = 1
print(max(note.values()))