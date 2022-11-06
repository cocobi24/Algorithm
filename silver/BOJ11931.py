# https://www.acmicpc.net/problem/11931

import sys
input = sys.stdin.readline
n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse=True)
print('\n'.join(map(str, nums)), end='')