# https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
dp = [sum(temp_list[:K])]

for i in range(N - K):
    dp.append(dp[i] - temp_list[i] + temp_list[K+i])

print(max(dp))