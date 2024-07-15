# https://www.acmicpc.net/problem/15688

import sys
input = sys.stdin.readline
n = int(input())
nums = map(str, sorted([int(input().rstrip()) for _ in range(n)]))
print('\n'.join(nums), end='')