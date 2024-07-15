# https://www.acmicpc.net/problem/28278

import sys
input = sys.stdin.readline
N = int(input())
stack = []

def processing (command, x = 0) :
  global stack
  if command == 1:
    # 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
    stack.append(x)
  elif command == 2:
    # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    print(stack.pop() if len(stack) > 0 else -1)
  elif command == 3:
    # 3: 스택에 들어있는 정수의 개수를 출력한다.
    print(len(stack))
  elif command == 4:
    # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
    print(1 if len(stack) == 0 else 0)
  else:
    # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    n = False
    if len(stack):
      n = stack.pop()
      stack.append(n)
    print(n if n else -1)

for _ in range(N):
  command, x = input().rstrip(), 0
  if len(command) > 1:
    command, x = map(int, command.split())
  else:
    command = int(command)
  processing(command, x)