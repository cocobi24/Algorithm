# https://www.acmicpc.net/problem/9237

from collections import deque
n = int(input())
trees = deque(sorted(list(map(int, input().split())), reverse=True))
answer = []

for i in range(n):
    answer.append(trees.popleft() + i)
print(max(answer) + 2, end='')