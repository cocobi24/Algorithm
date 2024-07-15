# https://www.acmicpc.net/problem/14469

import sys
input = sys.stdin.readline
n = int(input())
cows = [list(map(int, input().split())) for _ in range(n)]
cows.sort(key= lambda x : (x[0], x[1]))
time = cows[0][0] + cows[0][1]

for i in range(1, n) :
    if cows[i][0] >= time :
        time = cows[i][0] + cows[i][1]
    elif cows[i][0] < time :
        time += cows[i][1]

print(time)