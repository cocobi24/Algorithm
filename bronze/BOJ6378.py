# https://www.acmicpc.net/problem/6378

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n:
        while(n > 9):
            n = sum(map(int, list(str(n))))
        print(n)
    else:
        break