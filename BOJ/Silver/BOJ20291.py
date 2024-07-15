# https://www.acmicpc.net/problem/20291

import sys
input = sys.stdin.readline
n = int(input())
extends = {}

for i in range(n) :
    name, extend = input().rstrip().split('.')
    if extend in extends :
        extends[extend] += 1
    else :
        extends[extend] = 1

extends = sorted(extends.items(), key = lambda x : x[0])

for k, v in extends :
    print(k, v)