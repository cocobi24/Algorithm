# https://www.acmicpc.net/problem/2145

import sys
input = sys.stdin.readline

def number_game(num):
  if num < 10:
    return num
  n = sum(map(int, list(str(num))))
  return number_game(n)

while True:
  n = int(input())
  if n == 0:
    break
  print(number_game(n))