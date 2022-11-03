# https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline
n = int(input())
peoples = [list(map(int, input().split())) for i in range(n)]
answer = []

for i in range(n) :
    x, y = peoples[i]
    rank = 1
    for j in range(n) :
        xx, yy = peoples[j]
        if i == j :
            continue
        if xx > x and yy > y :
            rank += 1
    answer.append(rank)

print(*answer, end='')