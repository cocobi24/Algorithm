# https://www.acmicpc.net/problem/17254

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
key = [list(map(str, input().split())) for _ in range(M)]
key.sort(key=lambda x :(int(x[1]), int(x[0])))
[print(key[i][2], end='') for i in range(M)]