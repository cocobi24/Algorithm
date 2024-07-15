# https://www.acmicpc.net/problem/15650

import itertools
n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nPr = list(map(list, itertools.combinations(arr, m)))

for i in range(len(nPr)) :
    print(*nPr[i])