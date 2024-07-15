# https://www.acmicpc.net/problem/10211

import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    sum_list = [0] * n
    sum_list[0] = nums[0]

    for i in range(1, n) :
        sum_list[i] = max(sum_list[i-1] + nums[i], nums[i])
    print(max(sum_list))