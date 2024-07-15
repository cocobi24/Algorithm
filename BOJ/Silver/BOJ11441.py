# https://www.acmicpc.net/problem/11441

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
sum_list = [0]

for i in range(n) :
    sum_list.append(sum_list[i] + nums[i])

for _ in range(m) :
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])