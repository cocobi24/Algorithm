# https://www.acmicpc.net/problem/2010

import sys
input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n) :
    socket = int(input())
    answer += socket

answer = (answer - n) + 1
print(answer)
