# https://www.acmicpc.net/problem/8975

import sys
input = sys.stdin.readline
n = int(input())
lyrics = set(input().rstrip() for _ in range(n))
m = int(input())
target = [input().rstrip() for _ in range(m)]
l = n//2

ans = 0
for t in target:
  ans += 1
  if t in lyrics:
    lyrics.remove(t)
  if l >= len(lyrics):
    break
print(ans)