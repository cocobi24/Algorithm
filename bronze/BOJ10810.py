# https://www.acmicpc.net/problem/10810

import sys
input = sys.stdin. readline
n, m = map(int, input().split())
bucket = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j+1):
        bucket[idx-1] = k

print(*bucket)