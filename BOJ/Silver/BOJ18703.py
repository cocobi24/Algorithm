# https://www.acmicpc.net/problem/18703

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  files = {}
  for _ in range(N):
    name, id = map(str, input().rstrip().split())
    id = int(id)
    if name not in files:
      files[name] = id
    elif files[name] > id:
      files[name] = id
  files = sorted(files.values())
  print(*files)