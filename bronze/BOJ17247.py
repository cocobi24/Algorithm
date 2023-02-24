# https://www.acmicpc.net/problem/17247

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
check = []
coordinate = []

for i in range(N) :
    row = input().rstrip()
    if '1' in row :
        check.append(i)
    maps.append(list(row.split()))
    if len(check) == 2 :
        break

for idx in check :
    position = maps[idx].index('1')
    coordinate.append((idx, position))

answer = abs(coordinate[0][0] - coordinate[1][0]) + abs(coordinate[0][1] - coordinate[1][1])
print(answer)