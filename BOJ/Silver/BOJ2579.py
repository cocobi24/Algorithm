# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline
stairs = []
dp = []

n = int(input())
for _ in range(n):
    stairs.append(int(input()))

if n > 2:
    dp.append(stairs[0])
    dp.append(max(stairs[0]+stairs[1], stairs[1]))
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i - 1]))

    print(dp[-1], end='')
else :
    print(sum(stairs), end='')