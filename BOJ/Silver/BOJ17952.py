# https://www.acmicpc.net/problem/17952

import sys
input = sys.stdin.readline
N = int(input())

def fomula(min):
  global stack, sum_score
  min -= 1
  if min == 0:
    sum_score += score
  else:
    stack.append([_, score, min])

stack, sum_score = [], 0
for _ in range(N):
  obj = input().rstrip()
  if obj[0] == '0':
    if len(stack) > 0:
      _, score, min = stack.pop()
      fomula(min)
  else :
    _, score, min = map(int, obj.split())
    fomula(min)

print(sum_score)