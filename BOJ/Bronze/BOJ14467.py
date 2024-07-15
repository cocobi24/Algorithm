# https://www.acmicpc.net/problem/14467

import sys
input = sys.stdin.readline

N = int(input())
cow_set = {}
cross_cnt = 0
for _ in range(N):
  cow, flag = map(int, input().split())
  if cow not in cow_set:
    cow_set[cow] = flag
  elif cow_set[cow] != flag:
    cow_set[cow] = flag
    cross_cnt += 1

print(cross_cnt)