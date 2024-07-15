# https://www.acmicpc.net/problem/2303

import sys
input = sys.stdin.readline
n = int(input())
num_list = list(list(map(int, input().split())) for _ in range(n))
num_set = {}
i = 1
for nums in num_list :
    l = len(nums)
    temp = []
    for j in range(l-2) :
        for k in range(j+1, l-1) :
            for p in range(k+1, l) :
                total = nums[j] + nums[k] + nums[p]
                temp.append(total % 10)
    num_set[i] = max(temp)
    i += 1
num_set = sorted(num_set.items(), key = lambda x : (x[1], x[0]), reverse=True)
print(num_set[0][0])