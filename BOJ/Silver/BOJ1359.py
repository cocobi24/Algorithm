# https://www.acmicpc.net/problem/1359

from itertools import combinations
N, M, K = map(int, input().split())
myNum = 0
yourNum = 0
N = range(N)

for outer_comb in combinations(N, M):
    outer_set = set(outer_comb)

    for inner_comb in combinations(N, M):
        inner_set = set(inner_comb)
        myNum += 1

        if len(outer_set & inner_set) >= K:
            yourNum += 1

print(yourNum/myNum)