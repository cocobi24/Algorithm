# https://www.acmicpc.net/problem/16208

import sys
input = sys.stdin.readline
n = int(input())
nums = sorted(list(map(int, input().split())))
total = sum(nums)
answer = 0

for num in nums:
    answer += num * (total - num)
    total -= num
print(answer)