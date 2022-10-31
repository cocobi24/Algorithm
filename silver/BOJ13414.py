# https://www.acmicpc.net/problem/13414

import sys
input = sys.stdin.readline
k, l = map(int, input().split())
tables = {}

for i in range(l) :
    student = input().rstrip()
    if student not in tables :
        tables[student] = 1
    else :
        tables.pop(student)
        tables[student] = 1

tables = list(tables)

if len(tables) > k :
    for i in range(k) :
        print(tables[i])
else :
    print('\n'.join(tables))