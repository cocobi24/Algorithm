# https://www.acmicpc.net/problem/9507

def koong(n) :
    if n < 2 :
        return 1
    if n == 2 :
        return 2
    if n == 3 :
        return 4
    if dp[n] :
        return dp[n]
    dp[n] = koong(n-1) + koong(n-2) + koong(n-3) + koong(n-4)
    return dp[n]

n = int(input())
dp = [0] * 68
for _  in range(n) :
    x = int(input())
    print(koong(x))
