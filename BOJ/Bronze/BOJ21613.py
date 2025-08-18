# https://www.acmicpc.net/problem/21613

import sys
input = sys.stdin.readline

n = int(input().rstrip())
order = {}
for _ in range(n):
    name = input().rstrip()
    cost = int(input().rstrip())
    if cost in order:
        order[cost].append(name)
    else:
        order[cost] = [name]
max_cost = max(order)
print(order[max_cost][0])