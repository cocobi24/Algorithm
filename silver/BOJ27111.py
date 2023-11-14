# https://www.acmicpc.net/problem/27111

import sys
input = sys.stdin.readline
n = int(input())
record = set()
cnt = 0

for _ in range(n):
  a, b = map(int, input().split())
  if b == 1:
    if a in record:
      cnt += 1
    else:
      record.add(a)
  elif b == 0:
    if a not in record:
      cnt += 1
    else:
      record.remove(a)
cnt += len(record)
print(cnt)