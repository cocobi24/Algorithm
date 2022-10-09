# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(str, input().split()))
m = int(input())
checks = list(map(str, input().split()))
answer = {}

for i in checks :
    answer[i] = 0

for m in cards :
    if m in answer :
        answer[m] += 1

print(*answer.values())