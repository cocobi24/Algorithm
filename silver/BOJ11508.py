# https://www.acmicpc.net/problem/11508

import sys
input = sys.stdin.readline
n = int(input())
milk_list = sorted([int(input()) for i in range(n)], reverse=True)
answer = 0

for idx, milk in enumerate(milk_list, start=1):
    if idx % 3 == 0 :
        continue
    answer += milk
print(answer)