# https://www.acmicpc.net/problem/27110

n = int(input())
pick = list(map(int, input().split()))

ans = [0] * 3
for i in range(3):
  ans[i] = pick[i] if n >= pick[i] else n

print(sum(ans))