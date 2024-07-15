# https://www.acmicpc.net/problem/9009

n = int(input())
nums = [int(input()) for _ in range(n)]

dp = [i for i in range(51)]
for i in range(2, 51):
    dp[i] = dp[i - 1] + dp[i - 2]

dp = sorted(dp[1::], reverse=True)
for num in nums :
    answer = []
    for i in range(len(dp)) :
        answer.append(dp[i])
        if sum(answer) > num :
            answer.pop()
            continue
    print(*answer[::-1])