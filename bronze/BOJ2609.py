# https://www.acmicpc.net/problem/2609

import sys
input = sys.stdin.readline
x, y = map(int, input().split())

def gcb(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lem(a, b) :
    return int(a*b / gcb(a, b))

print(gcb(x, y))
print(lem(x, y))