# https://www.acmicpc.net/problem/14606

N = int(input())

ans = 0
for i in range(N - 1, 0, -1):
  ans += i
print(ans)