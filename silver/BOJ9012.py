# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline
n = int(input())

for i in range(n) :
    ps = list(input().rstrip())
    answer = []
    flag = 0

    for lps in ps :
        if lps == "(" :
            answer.append(lps)
        else :
            if len(answer) != 0:
                answer.pop()
            else :
                answer.append(lps)
                break

    if len(answer) == 0:
        print("YES")
    else :
        print("NO")
