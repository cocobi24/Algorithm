# https://www.acmicpc.net/problem/3135

import sys
input = sys.stdin.readline
a, b = map(int, input().split())
n = int(input())
frequencys = sorted([int(input()) for _ in range(n)])

min_checker = 1001
for i in range(n) :
    temp = abs(frequencys[i] - b)
    if min_checker > temp :
        min_checker = temp
        min_frequency = frequencys[i]

OPTION_A = abs(a-b)
OPTION_C = abs(min_frequency-b) + 1
print(OPTION_A if OPTION_A < OPTION_C else OPTION_C)