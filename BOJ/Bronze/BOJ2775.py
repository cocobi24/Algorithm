# https://www.acmicpc.net/problem/2775

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    k = int(input())
    n = int(input())
    floor_list = [x for x in range(1, n+1)]

    for _ in range(k) :
        for i in range(1, n) :
            floor_list[i] += floor_list[i-1]

    print(floor_list[-1])