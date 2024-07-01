# https://www.acmicpc.net/problem/14545

p = int(input())

for _ in range(p):
  l = int(input())
  ans = 0
  for i in range(1, l+1):
    ans += i ** 2
  print(ans)