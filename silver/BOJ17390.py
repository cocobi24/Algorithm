# https://www.acmicpc.net/problem/17390

import sys
input = sys.stdin.readline

a, n = map(int, input().split())
nums = sorted(list(map(int, input().split())))
sums = [0]
sum = 0

for i in range(a) :
    sum += nums[i]
    sums.append(sum)

for _ in range(n) :
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])
