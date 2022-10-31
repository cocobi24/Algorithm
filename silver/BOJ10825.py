# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline
n = int(input())
temp = []
for i in range(n) :
    name, lang, eng, math = input().rstrip().split()
    temp.append([name, int(lang), int(eng), int(math)])

temp.sort(key = lambda x :(-x[1], x[2], -x[3], x[0]))

for i in range(n) :
    print(temp[i][0])
