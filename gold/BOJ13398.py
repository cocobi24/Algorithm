# https://www.acmicpc.net/problem/13398

N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]
dp[0][0], dp[1][0] = nums[0], -1001
for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + nums[i], nums[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])

answer = max(max(dp[0]), max(dp[1]))
print(answer)