# https://www.acmicpc.net/problem/5430

from collections import deque
t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    queue = deque(input()[1:-1].split(','))
    flag = 0

    if n == 0:
        queue = []

    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(queue) == 0:
                print("error")
                break
            if flag % 2 == 0:
                queue.popleft()
            else:
                queue.pop()

    else:
        if flag % 2 == 0:
            answer = ",".join(queue)
            print("[" + answer + "]")
        else:
            queue.reverse()
            answer = ",".join(queue)
            print("[" + answer + "]")