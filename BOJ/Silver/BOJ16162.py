# https://www.acmicpc.net/problem/16162

N, A, D = map(int, input().split())
fitch = list(map(int, input().split()))
target, ans = A, 0

for i in range(N):
  if fitch[i] == target:
    target += D
    ans += 1
print(ans)