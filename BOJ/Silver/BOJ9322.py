# https://www.acmicpc.net/problem/9322

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  first = list(input().rstrip().split())
  second = list(input().rstrip().split())
  pwd = list(input().rstrip().split())
  decrypt = [[first.index(second[i]), pwd[i]] for i in range(n)]
  decrypt.sort()
  print(*[d[1] for d in decrypt])