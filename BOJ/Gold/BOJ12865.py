# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline
N, K = map(int, input().split())

item_list = [[0, 0]]
for _ in range(N):
    W, V = map(int, input().split())
    item_list.append([W, V])

inventory = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        W = item_list[i][0]
        V = item_list[i][1]
        inventory[i][j] = inventory[i-1][j] if j < W else max(V + inventory[i-1][j-W], inventory[i-1][j])

print(inventory[N][K])