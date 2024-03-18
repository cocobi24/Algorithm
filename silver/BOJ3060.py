# https://www.acmicpc.net/problem/3060

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  food = int(input())
  pig = list(map(int, input().split()))
  temp = pig.copy()
  day = 1
  total = sum(pig)
  while food >= total:
    day +=1
    pig[0] += temp[1] + temp[5] + temp[3]
    pig[1] += temp[0] + temp[2] + temp[4]
    pig[2] += temp[1] + temp[3] + temp[5]
    pig[3] += temp[2] + temp[4] + temp[0]
    pig[4] += temp[3] + temp[5] + temp[1]
    pig[5] += temp[0] + temp[4] + temp[2]
    temp = pig.copy()
    total = sum(pig)
  print(day)