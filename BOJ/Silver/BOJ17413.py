# https://www.acmicpc.net/problem/17413

from collections import deque
str_list = list(input())
queue = deque()
answer = ""
flag = 0

for s in str_list :
    if s == "<"  or s == ">" or s == " ":
        if s == "<" :
            flag = 1
        elif s == ">" :
            flag = 0

        if len(queue) > 0 :
            answer += ''.join(queue)
            queue.clear()
        answer += s
    else :
        if flag == 0 :
            queue.appendleft(s)
        elif flag == 1 :
            answer += s

if len(queue) > 0 :
    answer += ''.join(queue)
    queue.clear()

print(answer, end="")

