# https://www.acmicpc.net/problem/2870

import re
import sys
input = sys.stdin.readline
n = int(input())
nums = []

for _ in range(n) :
    s = input().rstrip()
    s = list(re.sub('[^0-9]', '\n', s).split())
    nums += s
answer = sorted(list(map(int, nums)))
print(*answer, sep='\n', end='')