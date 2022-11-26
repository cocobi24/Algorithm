# https://www.acmicpc.net/problem/1676

def factorial(n) :
    if n <= 1:
        return 1
    if dp[n] :
        return dp[n]
    dp[n] = n * factorial(n-1)
    return dp[n]

dp = [0] * 501
n = int(input())
s = str(factorial(n))
answer = 0

for i in range(1, len(s)+1) :
    if int(s[-i]) == 0 :
        answer += 1
    else :
        break

print(answer)