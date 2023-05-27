# https://www.acmicpc.net/problem/18110

import sys

def solved_round(num) :
    if num - int(num) >= 0.5 :
        return int(num) + 1
    return int(num)

input = sys.stdin.readline
n = int(input())

if n == 0 :
    print(0)
else :
    ranks = sorted(int(input()) for _ in range(n))
    check = solved_round(n * 0.15)

    if check != 0 :
        ranks = ranks[check: -check]

    cnt = n - 2 * check
    res = sum(ranks)
    answer = solved_round(res / cnt)
    print(answer)