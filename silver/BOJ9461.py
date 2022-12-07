# https://www.acmicpc.net/problem/9461

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

def triangle(n) :
    if dp[n] :
        return dp[n]
    dp[n] = triangle(n-2) + triangle(n-3)
    return dp[n]

for _ in range(int(input())) :
    n = int(input())
    print(triangle(n))
