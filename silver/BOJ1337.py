# https://www.acmicpc.net/problem/1337

import sys
input = sys.stdin.readline
N = int(input())
nums = sorted(int(input()) for _ in range(N))
answer = 5

for i in range(N) :
    cnt = 0
    for j in range(nums[i], nums[i]+5) :
        if j not in nums :
            cnt += 1
    answer = min(answer, cnt)

print(answer)