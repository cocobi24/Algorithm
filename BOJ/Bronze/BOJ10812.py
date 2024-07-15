# https://www.acmicpc.net/problem/10812

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
change = [list(map(int, input().split())) for _ in range(M)]
bucket = [i for i in range(1, N+1)]
for item in change:
  i, j, k = item
  i, k = i-1, k-1
  rotate = bucket[k:j]
  if len(rotate) < (j-i)+1:
    rotate += bucket[i:k]
  bucket[i:j] = rotate
print(*bucket)