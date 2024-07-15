# https://www.acmicpc.net/problem/6359

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    N = int(input())
    rooms = {i+1: 1 for i in range(N)}
    answer = 1

    for i in range(2, N+1) :
        for j in range(i,  N+1) :
            if j % i == 0 :
                rooms[j] += 1
        if rooms[i] % 2 != 0:
            answer += 1

    print(answer)