# https://www.acmicpc.net/problem/11866

from collections import deque
n, k = map(int, input().split())
queue = deque(i+1 for i in range(n))
answers = []

for i in range(n) :
    queue.rotate(-k+1)
    answers.append(queue.popleft())

answer = ', '.join(map(str, answers))
print(F'<{answer}>')