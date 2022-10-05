# https://www.acmicpc.net/problem/10845

import sys
input = sys.stdin.readline
n = int(input())
queue = []

def push(queue, x) :
    return queue.append(x)

def pop(queue) :
    if len(queue) == 0 :
        return print(-1)
    return print(queue.pop(0))

def size(queue) :
    return print(len(queue))

def empty(queue) :
    if len(queue) == 0:
        return print(1)
    return print(0)

def front(queue) :
    if len(queue) == 0:
        return print(-1)
    num = queue.pop(0)
    queue.insert(0, num)
    return print(num)

def back(queue) :
    if len(queue) == 0:
        return print(-1)
    num = queue.pop()
    queue.append(num)
    return print(num)

for i in range(n) :
    s = input().split()
    command = s[0]
    if command == "push" : push(queue, s[1])
    elif command == "pop" : pop(queue)
    elif command == "size": size(queue)
    elif command == "empty": empty(queue)
    elif command == "front" : front(queue)
    elif command == "back":  back(queue)