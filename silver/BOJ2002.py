# https://www.acmicpc.net/problem/2002

import sys
input = sys.stdin.readline
n = int(input())
in_list = [input().rstrip() for _ in range(n)]

cnt = 0
for _ in range(n):
  out_car = input().rstrip()
  if in_list[0] != out_car:
    cnt += 1
  in_list.remove(out_car)

print(cnt)