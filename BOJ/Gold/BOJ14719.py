# https://www.acmicpc.net/problem/14719

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
blocks = list(map(int, input().split()))
world = [[0 for j in range(y)] for i in range(x)]
answer = 0

for j in range(y) :
    block = blocks[j]
    flag = x - block -1
    for i in range(x-1, flag, -1):
        world[i][j] = 1

for i in range(x) :
    row = world[i]
    try :
        firstIndex = row.index(1)
        lastIndex = y - row[y::-1].index(1)
        for j in range(firstIndex, lastIndex-1) :
            if world[i][j] == 0 :
                answer += 1
    except :
        continue

print(answer)