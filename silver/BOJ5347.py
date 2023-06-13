# https://www.acmicpc.net/problem/5347

import sys
input = sys.stdin.readline
n = int(input())

def gcd(x, y) :
    while y > 0 :
        temp = y
        y, x = x % y, temp
    return x

for _ in range(n) :
    a, b = map(int, input().split())
    answer = (a*b) // gcd(a,b)
    print(answer)