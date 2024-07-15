# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lan = list(int(input()) for _ in range(K))
start, end = 1, max(lan)

while start <= end:
  mid = (start + end) // 2
  count = 0
  for i in range(K):
    count += lan[i] // mid

  if count >= N:
    start = mid + 1
  else:
    end = mid - 1

print(end)