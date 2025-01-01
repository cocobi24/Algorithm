# https://www.acmicpc.net/problem/18679

import sys
input = sys.stdin.readline

N = int(input())
dict = {}
for _ in range(N):
    x, y = input().rstrip().split(' = ')
    dict[x] = y

T = int(input())
for _ in range(T):
    K = int(input())
    word = input().rstrip().split()
    for w in word:
        print(dict[w], end=' ')
    print()