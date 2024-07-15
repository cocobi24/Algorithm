# https://www.acmicpc.net/problem/14891

from collections import deque
import sys
input = sys.stdin.readline
gear = [deque(map(int, input().rstrip())) for _ in range(4)]

k = int(input())
for i in range(k):
  num, direction = map(int, input().split())
  num -= 1

  front, rear = [], []
  for i in range(num, 0, -1):
    if gear[i][6] != gear[i-1][2]:
      front.append(i-1)
    else:
      break

  for i in range(num, 3):
    if gear[i][2] != gear[i+1][6]:
      rear.append(i+1)
    else:
      break
  gear[num].rotate(direction)

  fd, rd = direction * -1, direction * -1
  for i in range(len(front)):
    gear[front[i]].rotate(fd)
    fd *= -1

  for i in range(len(rear)):
    gear[rear[i]].rotate(rd)
    rd *= -1
point = [1, 2, 4, 8]
ans = [0] * 4

for i in range(4):
  if gear[i][0] == 1:
    ans[i] = point[i]

print(sum(ans))