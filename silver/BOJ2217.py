# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline
n = int(input())
ropes = sorted((int(input()) for _ in range(n)), reverse=True)
answer = [ropes[i]*(i+1) for i in range(n)]
print(max(answer), end='')