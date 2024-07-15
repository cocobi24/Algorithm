# https://www.acmicpc.net/problem/2547

import sys
input = sys.stdin.readline
answer = []
n = int(input())

for i in range(n) :
    temp = input()
    m = int(input())
    sum = 0
    for j in range(m) :
        candy = int(input())
        sum += candy
    if sum % m == 0 :
        answer.append("YES")
    else :
        answer.append("NO")

print('\n'.join(answer))