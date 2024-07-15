# https://www.acmicpc.net/problem/1535

n = int(input())
J = [0] + list(map(int, input().split()))
L = [0] + list(map(int, input().split()))

dp = [[0] * 101 for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, 101):
    if J[i] <= j:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-J[i]] + L[i])
    else:
      dp[i][j] = dp[i-1][j]

answer = dp[n][99]
print(answer)