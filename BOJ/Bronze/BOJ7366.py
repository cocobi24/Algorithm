# https://www.acmicpc.net/problem/7366

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    M = int(input())
    s_list = input().rstrip().split()
    count = 0
    for s in s_list:
        if s == 'sheep':
            count += 1
    print(f'Case {_ + 1}: This list contains {count} sheep.\n')