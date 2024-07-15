# https://www.acmicpc.net/problem/1758

def fibo(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    if dp[n] :
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n -2)
    return dp[n]

dp = [0] * 41
t = int(input())
for _ in range(t) :
    n = int(input())
    if n == 0 :
        print(1,0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibo(n-1), fibo(n))