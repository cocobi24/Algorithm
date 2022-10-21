# https://www.acmicpc.net/problem/1475

import math
num = list(input())
l = len(num)
answer = {}

for n in num :
    n = int(n)
    if n == 9 :
        n = 6
    if n not in answer :
        answer[n] = 1
    else :
        answer[n] += 1

if 6 in answer :
    answer[6] /= 2
    answer[6] = math.ceil(answer[6])

answer = sorted(answer.items(), key = lambda x : x[1], reverse=True)
print(answer[0][1], end='')