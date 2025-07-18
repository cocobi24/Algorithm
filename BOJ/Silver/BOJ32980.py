# https://www.acmicpc.net/problem/32980

import sys
input = sys.stdin.readline

N = int(input())
garbage = list(input().rstrip() for _ in range(N))
cost = list(map(int, input().split()))

cost_set, idx = {'O': int(input())}, 0
for g in ['P', 'C', 'V', 'S', 'G', 'F']:
    cost_set[g] = min(cost[idx], cost_set['O'])
    idx += 1

ans = 0
for g in garbage:
    g_types = len(set(g))
    if g_types > 1:
        ans += len(g) * cost_set['O']
    else:
        ans += len(g) * min(cost_set[g[0]], cost_set['O'])
print(ans)