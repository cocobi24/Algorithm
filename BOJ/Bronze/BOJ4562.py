# https://www.acmicpc.net/problem/4562

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  x, y = map(int, input().rstrip().split())
  print("MMM BRAINS" if x >= y else "NO BRAINS")