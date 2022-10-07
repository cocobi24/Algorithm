# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]
coins.reverse()
temp = []
answer = 0

for i in range(n) :
    if coins[i] > k :
        temp.append(coins[i])

searchIndex = len(temp)

for i in range(searchIndex, n) :
    answer += k // coins[i]
    k = k % coins[i]

print(answer)