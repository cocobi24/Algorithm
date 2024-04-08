# https://www.acmicpc.net/problem/11649

import sys
input = sys.stdin.readline
n = int(input())
words = sorted(input().rstrip()[::-1] for _ in range(n))
print(*words, sep='\n')