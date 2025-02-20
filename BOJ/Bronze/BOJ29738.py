# https://www.acmicpc.net/problem/29738

import sys
input = sys.stdin.readline
T = int(input()) + 1

def getRound(n):
  if n > 4500:
    return "Round 1"
  if n > 1000:
    return "Round 2"
  if n > 25:
    return "Round 3"
  return "World Finals"

for i in range(1, T):
  n = int(input())
  print(f"Case #{i}: {getRound(n)}")