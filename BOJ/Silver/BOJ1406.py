# https://www.acmicpc.net/problem/1406

import sys
from collections import deque
input = sys.stdin.readline
s = input().rstrip()
n = int(input())
left, right = list(s), deque()

for _ in range(n):
  command = input().rstrip()
  if command[0] == 'P':
    left.append(command[2])
  elif command == 'L' and len(left) > 0:
    right.appendleft(left.pop())
  elif command == 'D' and len(right) > 0:
    left.append(right.popleft())
  elif command == 'B' and len(left) > 0:
    left.pop()
print(''.join(left + list(right)))