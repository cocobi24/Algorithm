# https://www.acmicpc.net/problem/13371

import sys, math
input = sys.stdin.readline

def getSequence(x):
  return math.ceil((-1 + math.sqrt(1 + 8 * x / 3)) / 2)

def getPosition(x, n):
  return x - (3 * n * (n - 1) // 2)

T = int(input())
for _ in range(T):
  n  = int(input())
  sequence = getSequence(n)
  position = getPosition(n, sequence)
  idx = math.ceil(position/sequence)

  dolphin, jump = "dolphins", "jumps"
  if sequence == 1:
    dolphin = "dolphin"
    jump = "jump"

  if idx == 1:
    print(f"{sequence} {dolphin}")
  elif idx == 2:
    print(f"{sequence} {jump}")
  else:
    print("splash")