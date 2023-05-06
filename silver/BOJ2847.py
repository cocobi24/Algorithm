# https://www.acmicpc.net/problem/2847

import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
cur = nums.pop()
nums.reverse()

answer = 0
for num in nums :
    if cur <= num :
        minus = (num+1) - cur
        answer += minus
        cur = num-minus
    else :
        cur = num

print(answer)