# https://www.acmicpc.net/problem/1966

import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    n, m  = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    print_queue = deque((index, value) for index, value in enumerate(nums))
    target_importace = print_queue[m][1]
    target_number = print_queue[m][0]
    l = len(nums)

    while True :
        importance = max(nums)
        first = print_queue.popleft()
        temp = nums.popleft()

        if first[1] < importance :
            print_queue.append(first)
            nums.append(temp)
        else :
            if first[0] == target_number :
                print(l - len(print_queue))
                break
