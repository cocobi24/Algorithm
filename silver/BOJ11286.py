# https://www.acmicpc.net/problem/11286

import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
queue = PriorityQueue()

for _ in range(n) :
    num = int(input())
    if num != 0 :
        queue.put((abs(num), num))
    elif queue.qsize() == 0 :
        print(0)
    else :
        print(queue.get()[1])