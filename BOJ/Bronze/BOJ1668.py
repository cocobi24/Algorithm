# https://www.acmicpc.net/problem/1668

import sys
input = sys.stdin.readline
N = int(input())
left_trophy = [int(input()) for _ in range(N)]
right_trophy  = left_trophy.copy()
right_trophy.reverse()

left, left_max, right, right_max = 0, 0, 0, 0
for i in range(N) :
    if left_max < left_trophy[i] :
        left += 1
        left_max = left_trophy[i]

    if right_max < right_trophy[i] :
        right += 1
        right_max = right_trophy[i]

print(left, right, sep="\n")