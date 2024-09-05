# https://www.acmicpc.net/problem/17829

import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

while len(grid) > 1:
  newGrid = []
  idx = 0
  for i in range(0, N, 2):
    newGrid.append([])
    for j in range(0, len(grid[i])-1, 2):
      x = sorted(grid[i][j:j+2] + grid[i+1][j:j+2])[2]
      newGrid[idx].append(x)
    idx += 1
  grid = newGrid
  N = len(grid)
print(grid[0][0])