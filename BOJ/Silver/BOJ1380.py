# https://www.acmicpc.net/problem/1380

import sys
input = sys.stdin.readline

scenario = 1
while True:
  n = int(input())
  earrings = set()

  if n == 0:
    break

  names = [input().rstrip() for _ in range(n)]
  for _ in range(2 * n - 1):
    num, _ = map(str, input().rstrip().split())
    if num not in earrings:
      earrings.add(num)
    else:
      earrings.remove(num)

  print(f"{scenario} {names[int(*earrings)-1]}")
  scenario += 1