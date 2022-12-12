# https://www.acmicpc.net/problem/11557

import sys
input = sys.stdin.readline
t = int(input())
answer = ''

for _ in range(t) :
    n = int(input())
    consume = 0

    for _ in range(n) :
        univ, l = map(str, input().split())
        l = int(l)
        if l > consume :
            consume = l
            answer = univ
    print(answer)
