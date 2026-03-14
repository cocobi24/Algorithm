# https://www.acmicpc.net/problem/33868

N = int(input())

maxT, minB = 0, 9999
for _ in range(N):
  T, B = map(int, input().split())
  maxT = max(maxT, T)
  minB = min(minB, B)
number = (maxT * minB) % 7
print(number + 1)