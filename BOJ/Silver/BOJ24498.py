# https://www.acmicpc.net/problem/24498

N = int(input())
blob = list(map(int, input().split()))

tower = 0
for i in range(1, N-1):
  min_blob = min(blob[i-1], blob[i+1])
  tower = max(blob[i] + min_blob, tower)
print(max(blob[0], tower, blob[-1]))