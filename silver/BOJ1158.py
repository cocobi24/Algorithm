# https://www.acmicpc.net/problem/1158

from collections import deque
n, k = map(int, input().split())
queue = deque([i+1 for i in range(n)])
answer = deque()

while True :
    if len(queue) == 0 :
        break
    queue.rotate(-(k-1))
    answer.append(queue.popleft())

answer = ', '.join(map(str,answer))
print(F"<{answer}>", end='')