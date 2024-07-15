# https://www.acmicpc.net/problem/1235

import sys
input = sys.stdin.readline
n = int(input())
nums = [input().rstrip() for _ in range(n)]
k = 0

while True :
    k += 1
    temp = []
    for num in nums :
        if num[-k:] not in temp :
            temp.append(num[-k:])
        else :
            continue
    if len(temp) == len(nums) :
        break

print(k, end='')