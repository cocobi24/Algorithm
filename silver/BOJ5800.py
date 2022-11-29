# https://www.acmicpc.net/problem/5800

import sys
input = sys.stdin.readline
n = int(input())
class_list = []
gap_list = []

for i in range(n) :
    nums = list(map(int, input().split()))
    m = nums[0]
    class_list.append([])

    for j in range(1, m+1) :
        class_list[i].append((nums[j]))

    class_list[i].sort(reverse=True)

    large_gap = class_list[i][0] - class_list[i][1]

    for k in range(2, m) :
        gap = class_list[i][k-1] - class_list[i][k]
        if gap > large_gap :
            large_gap = gap

    print(F"Class {i+1}")
    print(F"Max {max(class_list[i])}, Min {min(class_list[i])}, Largest gap {large_gap}")