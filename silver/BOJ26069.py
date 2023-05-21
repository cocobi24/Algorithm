# https://www.acmicpc.net/problem/26069

import sys
input = sys.stdin.readline
N = int(input())
ChongChong_set = {"ChongChong": True}

for _ in range(N) :
    A, B = map(str, input().split())

    if A in ChongChong_set :
        ChongChong_set[B] = True
    elif B in ChongChong_set :
        ChongChong_set[A] = True

print(len(ChongChong_set))