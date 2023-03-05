# https://www.acmicpc.net/problem/1051

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = [list(input().rstrip()) for _ in range(n)]

square = 1
for i in range(n):
    for j in range(m):
        for k in range(square, 50):
            if n <= i+k or m <= j+k:
                break
            if len(set([nums[i][j], nums[i+k][j], nums[i][j+k], nums[i+k][j+k]])) == 1:
                square = max(square, k+1)

answer = square**2
print(answer)