# https://www.acmicpc.net/problem/25757

import sys
input = sys.stdin.readline
n, game = map(str, input().split())
player = list(set(input().strip() for _ in range(int(n))))
if game == 'Y':
  req = 1
elif game == 'F':
  req = 2
else:
  req = 3
print(len(player) // req)