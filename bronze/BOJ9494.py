# https://www.acmicpc.net/problem/9494

import sys
input = sys.stdin.readline

while True:
  T = int(input().rstrip())

  if T == 0:
    break

  answer = 0
  for i in range(T):
    text = input().rstrip() + " "
    idx = []
    for j in range(len(text)):
      if text[j] == ' ': idx.append(j+1)
    if i == 0: 
      answer = idx[0]
    idx = list(filter(lambda x: x >= answer, idx))
    if len(idx) > 0: 
      answer = idx[0]

  print(answer)