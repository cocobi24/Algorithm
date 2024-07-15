# https://www.acmicpc.net/problem/2346

from collections import deque
n = int(input())
nums = list(map(int, input().split()))
queue = deque()

for i in range(n) :
    queue.append((nums[i], i+1))

target = 0
while queue :
    target, answer = queue.popleft()

    if target > 0:
        queue.rotate(1 - target)
    else:
        queue.rotate(-(target))

    print(answer, end=" ")