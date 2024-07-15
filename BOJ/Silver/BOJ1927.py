# https://www.acmicpc.net/problem/1927

import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
queue = PriorityQueue()

for i in range(n) :
    num = int(input())
    if num == 0 :
        if queue.qsize() == 0 :
            print(0)
        else :
            min = queue.get(0)
            print(min)
    else :
        queue.put(num)