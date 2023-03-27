# https://www.acmicpc.net/problem/1911

import sys, math
input = sys.stdin.readline
N, L = map(int, input().split())
pool_list = sorted([list(map(int, input().split())) for _ in range(N)])

cnt, max_idx = 0, 0
for start, end in pool_list:
    if start <= max_idx:
        start = max_idx+1
        if end <= start:
            continue
    cur = math.ceil((end-start)/L)
    cnt += cur
    max_idx = max(max_idx, start + (cur*L) - 1)

print(cnt)