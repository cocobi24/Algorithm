# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
temp = []
answer = 0

for i in range(n) :
    str = input().rstrip()
    temp.append(str)

for i in range(m) :
    str = input().rstrip()
    if str in temp :
        answer += 1

print(answer, end='')