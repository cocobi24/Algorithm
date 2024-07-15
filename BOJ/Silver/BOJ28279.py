# https://www.acmicpc.net/problem/28279

import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()

def processing(command, x):
  n, l = None, len(queue)
  if command == 1:
    return queue.appendleft(x)
  elif command == 2:
    return queue.append(x)
  elif command == 3:
    return print(queue.popleft() if l > 0 else -1)
  elif command == 4:
    return print(queue.pop() if l > 0 else -1)
  elif command == 5:
    return print(l)
  elif command == 6:
    return print(0 if l > 0 else 1)
  elif command == 7 and l > 0:
    n = queue.popleft()
    queue.appendleft(n)
  elif command == 8 and l > 0:
    n = queue.pop()
    queue.append(n)
  return print(n if n is not None else -1)

for _ in range(N):
  command, x = input().rstrip(), 0
  if command[0] in ['1', '2']:
    command, x = map(int, command.split())
  else:
    command = int(command)
  processing(command, x)
