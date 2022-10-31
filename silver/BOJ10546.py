# https://www.acmicpc.net/problem/10546

import sys
input = sys.stdin.readline
n = int(input())
names = {}

for i in range(n + n - 1) :
    name = input().rstrip()
    if name not in names:
        names[name] = 1
    else :
        names[name] += 1

names = list(filter(lambda x : x[1] % 2 != 0, names.items()))
print(names[0][0], end='')