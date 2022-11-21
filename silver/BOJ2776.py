# https://www.acmicpc.net/problem/2776

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n = int(input())
    n_set = set(map(int, input().split()))
    m = int(input())
    m_set = list(map(int, input().split()))
    for num in m_set :
        if num in n_set :
            print(1)
        else :
            print(0)