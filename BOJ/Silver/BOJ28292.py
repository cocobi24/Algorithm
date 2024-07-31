# https://www.acmicpc.net/problem/28292

n = int(input())
ans = 0
if n <= 2:
  ans = 1
elif n < 6:
  ans = 2
else:
  ans = 3
print(ans)