# https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    revenue, maxStock = 0, 0
    for i in range(N-1, -1, -1):
        if stock[i] > maxStock:
            maxStock = stock[i]
        else:
            revenue += maxStock - stock[i]
    print(revenue)