# https://www.acmicpc.net/submit/11024

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  print(sum(list(map(int, input().split()))))