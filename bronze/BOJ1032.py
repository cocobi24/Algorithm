# https://www.acmicpc.net/problem/1032

import sys
input = sys.stdin.readline
n = int(input())
answers = []
answer = ''

for i in range(n) :
    str = list(input().rstrip())
    answers.append(str)

l = len(answers[0])
for j in range(l) :
    temp = {}
    s = ''
    for i in range(n) :
        s = answers[i][j]
        if s not in temp :
            temp[s] = 1
        else :
            temp[s] += 1
    if len(temp) == 1 :
        answer += s
    else :
        answer += '?'

print(answer)