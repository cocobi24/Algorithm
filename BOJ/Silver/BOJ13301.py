# https://www.acmicpc.net/problem/13301

n = int(input())

d = [0] * 81
d[0], d[1] = 4, 6
for i in range(2, n + 1):
  d[i] = d[i-1] + d[i-2]
print(d[n-1])