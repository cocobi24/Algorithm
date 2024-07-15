# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline
N = int(input())
minus_list, plus_list = [], []
answer = 0

for _ in range(N) :
    num = int(input())
    if num <= 0 :
        minus_list.append(num)
    elif num > 1 :
        plus_list.append(num)
    else :
        answer += 1

minus_list.sort()
plus_list.sort(reverse=True)

for i in range(0, len(plus_list), 2):
    if i+1 >= len(plus_list):
        answer += plus_list[i]
        continue
    answer += (plus_list[i] * plus_list[i+1])

for i in range(0, len(minus_list), 2):
    if i+1 >= len(minus_list):
        answer += minus_list[i]
        continue
    answer += (minus_list[i] * minus_list[i+1])

print(answer)