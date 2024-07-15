# https://www.acmicpc.net/problem/18258

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n) :
    row = list(input().split())
    cmd = row[0]
    if len(row) > 1 :
        if cmd == "push" :
            queue.append(row[1])
    else :
        if cmd == "pop" :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue.popleft())
        elif cmd == "size" :
            print(len(queue))
        elif cmd == "empty" :
            if len(queue) == 0 :
                print(1)
            else :
                print(0)
        elif cmd == "front" :
            if len(queue) == 0 :
                print(-1)
            else :
                print(queue[0])
        elif cmd == "back":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])