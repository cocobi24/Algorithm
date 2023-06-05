# https://www.acmicpc.net/problem/17608

import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
answer = 1
front = nums[-1]

for _ in range(N) :
    num = nums.pop()
    if front < num :
        answer += 1
        front = num
print(answer)