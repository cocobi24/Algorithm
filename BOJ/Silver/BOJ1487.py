# https://www.acmicpc.net/problem/1487

import sys
input = sys.stdin.readline
n = int(input())
cost_list = []

for _ in range(n):
    cost, deliv_cost = map(int, input().split())
    cost_list.append([cost, deliv_cost])

cost_list.sort(key=lambda x: (x[0], x[1]))
total = [0] * n

for i in range(n):
    for j in range(i, n):
        profit = cost_list[i][0] - cost_list[j][1]
        if profit > 0:
            total[i] += profit

answer = [cost_list[i][0] for i in range(n) if total[i] == max(total)]

if sum(total) == 0:
    print(0, end='')
else:
    print(min(answer), end='')