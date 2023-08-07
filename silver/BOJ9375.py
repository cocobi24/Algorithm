# https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    n = int(input())
    closet = {}
    for _ in range(n) :
        wear, category = map(str, input().split())
        if category not in closet :
            closet[category] = [wear]
        else :
            closet[category].append(wear)

    comb = 1
    for i in closet :
        category_length = len(closet[i])
        comb *= category_length + 1
    comb -= 1

    print(comb)