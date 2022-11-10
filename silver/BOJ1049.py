# https://www.acmicpc.net/problem/1049

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
set_cost = []
short_cost = []

for _ in range(m) :
    sets, shorts = map(int, input().split())
    set_cost.append(sets)
    short_cost.append(shorts)

set_cost.sort()
short_cost.sort()

max = set_cost[0] if set_cost[0] <= (short_cost[0]*6) else short_cost[0]*6
min = short_cost[0]
answer = ((n//6)*max) + ((n%6)*min)

if (n%6)*min > max :
    answer = ((n // 6) * max) + max

print(answer, end='')