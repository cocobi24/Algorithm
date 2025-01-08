# https://www.acmicpc.net/problem/31821

N = int(input())
menu = [int(input()) for _ in range(N)]

cost = 0
M = int(input())
for _ in range(M):
  pick = int(input()) - 1
  cost += menu[pick]
print(cost)