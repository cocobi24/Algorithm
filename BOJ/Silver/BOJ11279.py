# https://www.acmicpc.net/problem/11279

import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
queue = PriorityQueue()

for i in range(n) :
    num = int(input())
    if num == 0 :
        size = queue.qsize()
        if size == 0 :
            print(0)
        else :
            max = queue.get()[1]
            print(max)
    else :
        queue.put((-num, num))