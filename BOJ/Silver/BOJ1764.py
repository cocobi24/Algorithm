# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = {}

for i in range(n) :
    s = input().rstrip()
    if s not in answer :
        answer[s] = 1

for i in range(m) :
    s = input().rstrip()
    if s in answer:
        answer[s] += 1

answer = sorted(answer.items(), key=lambda x : (-x[1],x[0]))
answer = list(filter(lambda x: x[1] == 2, answer))
print(len(answer))

for k, v in answer :
    print(k)