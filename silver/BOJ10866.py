# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n = int(input())

for i in range(n) :
    str = input().split()
    command = str[0]
    if command == "push_front" :
        queue.appendleft(str[1])
    elif command == "push_back" :
        queue.append(str[1])
    elif command == "pop_front" :
        if len(queue) == 0:
            print(-1)
            continue
        num = queue.popleft()
        print(num)
    elif command == "pop_back" :
        if len(queue) == 0:
            print(-1)
            continue
        num = queue.pop()
        print(num)
    elif command == "size" :
        print(len(queue))
    elif command == "empty" :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif command == "front" :
        if len(queue) == 0:
            print(-1)
            continue
        num = queue.popleft()
        queue.appendleft(num)
        print(num)
    elif command == "back" :
        if len(queue) == 0:
            print(-1)
            continue
        num = queue.pop()
        queue.append(num)
        print(num)