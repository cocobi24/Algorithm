# https://www.acmicpc.net/problem/3058

import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n) :
    nums = list(map(int, input().split()))
    nums = list(filter(lambda x : x % 2 == 0, nums))
    print(sum(nums), min(nums))