# https://www.acmicpc.net/problem/20376

import sys
input = sys.stdin.readline
logs = set()
while True:
  log = input().rstrip()
  if len(log) == 0:
    break
  logs.add(log[11:])
print(len(logs))