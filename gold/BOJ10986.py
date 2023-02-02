# https://www.acmicpc.net/problem/10986

n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * m
dp[0] = 1

total = 0
for i in range(n):
    total += nums[i]
    r = total % m
    dp[r] += 1

answer = 0
for i in dp:
    answer += i * (i-1) // 2

print(answer)