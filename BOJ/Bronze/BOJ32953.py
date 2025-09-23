# https://www.acmicpc.net/problem/32953

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
attend_set = {}
for _ in range(N):
    class_n = int(input())
    std_num = map(int, input().split())
    for num in std_num:
        if num in attend_set:
            attend_set[num] += 1
        else:
            attend_set[num] = 1

ans = 0
for v in attend_set.values():
    if v >= M:
        ans += 1
print(ans)