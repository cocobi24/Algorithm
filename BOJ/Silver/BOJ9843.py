# https://www.acmicpc.net/problem/9843

import sys
input = sys.stdin.readline

def lvm_execute(commands):
  stack = []
  register = 0
  idx = 0

  while idx < len(commands):
    command = commands[idx].split()
    if command[0] == "PUSH":
      stack.append(int(command[1]))
    elif command[0] == "STORE":
      register = stack.pop()
    elif command[0] == "LOAD":
      stack.append(register)
    elif command[0] == "PLUS":
      stack.append(stack.pop() + stack.pop())
    elif command[0] == "TIMES":
      stack.append(stack.pop() * stack.pop())
    elif command[0] == "IFZERO":
      if stack.pop() == 0:
        idx = int(command[1])
        continue
    else:
      print(stack.pop())
      exit()

    idx += 1

n = int(input())
command = [input().rstrip() for _ in range(n)]
lvm_execute(command)