# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())
answer = []
for i in range(n) :
    num = int(input())
    answer.append(num)

answer.sort()
print('\n'.join(map(str, answer)))