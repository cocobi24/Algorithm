# https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
  mid = (start + end) // 2
  total = 0
  for tree in trees:
    if tree > mid:
      total += tree - mid

  if total >= M:
    start = mid + 1
  else:
    end = mid - 1
print(end)