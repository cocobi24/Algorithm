# https://www.acmicpc.net/problem/22403

import sys
input = sys.stdin.readline
N = int(input())

stack, answer = [], True
for _ in range(N):
  word = input().rstrip()
  if word == "A":
    stack.append(word)
  else:
    if len(stack):
      stack.pop()
    else:
      answer = False
      break
print("YES" if answer and len(stack) == 0 else "NO")