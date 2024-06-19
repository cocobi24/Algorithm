# https://www.acmicpc.net/problem/1813

n = int(input())
charm = list(map(int, input().split()))
ans = -1
for i in range(n + 1):
  if charm.count(i) == i:
    ans = i
print(ans)