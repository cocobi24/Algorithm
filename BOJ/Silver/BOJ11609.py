# https://www.acmicpc.net/problem/11609

import sys
input = sys.stdin.readline
n = int(input())
names = list(input().rstrip().split() for _ in range(n))
sorted_names = sorted(names, key=lambda x: (x[1], x[0]))

for name in sorted_names:
  print(name[0], name[1])