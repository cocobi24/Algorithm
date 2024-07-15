# https://www.acmicpc.net/problem/25192

import sys
input = sys.stdin.readline
n = int(input())
chat_logo = []
answer = 0

for _ in range(n) :
    message = input().rstrip()
    if message == "ENTER" :
        answer += len(set(chat_logo))
        chat_logo = []
    else :
        chat_logo.append(message)

answer = answer + len(set(chat_logo))
print(answer)