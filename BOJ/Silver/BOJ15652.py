# https://www.acmicpc.net/problem/15652

import itertools
n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
nPr = list(map(list, itertools.combinations_with_replacement(arr, m)))

for i in range(len(nPr)) :
    print(*nPr[i])