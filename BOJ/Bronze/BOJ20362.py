# https://www.acmicpc.net/problem/20362

import sys
input = sys.stdin.readline

N, S = input().split()
chat_list = []
answer = ''
for _ in range(int(N)):
    nick, chat = input().split()
    if nick != S:
        chat_list.append(chat)
    else:
        answer = chat
        break

chat_list = list(filter(lambda x: x == answer, chat_list))
print(len(chat_list))