# https://www.acmicpc.net/problem/30031

N = int(input())

def getMoney(mm):
  if mm == 136:
    return 1000
  if mm == 142:
    return 5000
  if mm == 148:
    return 10000
  if mm == 154:
    return 50000

ans = 0
for _ in range(N):
  mm, _ = map(int, input().split())
  ans += getMoney(mm)
print(ans)