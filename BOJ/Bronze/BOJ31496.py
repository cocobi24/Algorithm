# https://www.acmicpc.net/problem/31496

import sys
input = sys.stdin.readline

N, S = map(str, input().split())
N = int(N)

count = 0
for _ in range(N):
    items, qty = input().split()
    qty = int(qty)

    item_list = items.split('_')
    for item in item_list:
        if item == S:
            count += qty
            break
print(count)