# https://www.acmicpc.net/problem/5648

import sys
input = sys.stdin
nums = []
flag = 0
for i in input :
    num_list = list(map(int, i.rstrip()[::-1].split()))
    if flag == 0 :
        num_list.pop(-1)
        flag = 1
    nums += num_list
nums = sorted(nums)
print(*nums, sep="\n")