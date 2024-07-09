# https://www.acmicpc.net/problem/22233

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
keyword = set(input().rstrip() for _ in range(N))

for _ in range(M):
  post = set(map(str, input().rstrip().split(',')))
  for p in post:
    if p in keyword:
      keyword.remove(p)
  print(len(keyword))