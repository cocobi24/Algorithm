# https://www.acmicpc.net/problem/2502

d, k = map(int, input().split())
dp = [0] * d
dp[0], dp[1] = 1, 1

while dp[-1] != k:
  for i in range(2, d):
    dp[i] = dp[i-2]+dp[i-1]

  if dp[-1] > k:
    dp[0] += 1
    dp[1] = dp[0]
  elif dp[-1] < k:
    dp[1] += 1
  else:
    print(dp[0], dp[1], sep="\n")