# https://www.acmicpc.net/problem/2798

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = []

for i in range(n) :
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = nums[i] + nums[j] + nums[k]
            if sum <= m :
                sums.append(sum)

print(max(sums))