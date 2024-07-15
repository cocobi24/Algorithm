# https://www.acmicpc.net/problem/2607

import sys
input = sys.stdin.readline
n = int(input())
target = list(input().rstrip())
answer = 0

for _ in range(n-1):
    compare = target[:]
    words = input().rstrip()
    cnt = 0

    for word in words:
        if word in compare:
            compare.remove(word)
        else:
            cnt += 1

    if cnt < 2 and len(compare) < 2:
        answer += 1

print(answer)