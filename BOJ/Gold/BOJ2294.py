# https://www.acmicpc.net/problem/2294

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] + [10001] * k
for c in coin:
    for i in range(c, k+1):
        if dp[i] > 0:
            dp[i] = min( dp[i], dp[i-c]+1 )

print(dp[k] if dp[k] != 10001 else -1)