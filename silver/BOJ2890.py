# https://www.acmicpc.net/problem/2890

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
ranks = []
answer = []
nums = [i for i in range(1,10)]

for _ in range(r) :
    line = list(input().rstrip())
    line.pop()
    line.reverse()
    temp = 0
    for i in line :
        if i == '.' :
            temp += 1
        elif i != 'S' :
            ranks.append((i, temp))
            break

ranks.sort(key = lambda x : x[1])
rank = 1
prev = ranks[0][1]
for k, v in ranks :
    if prev < v :
        rank += 1
    answer.append((k, rank))
    prev = v

answer.sort(key = lambda x : x[0])
for k, v in answer :
    print(v)