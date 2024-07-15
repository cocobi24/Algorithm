# https://www.acmicpc.net/problem/10813

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bucket = [int(i) for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    temp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = temp

print(*bucket)