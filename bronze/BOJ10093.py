# https://www.acmicpc.net/problem/10093

a, b = map(int, input().split())

if a == b:
 print(0)
else:
  temp = max(a, b)
  a, b = min(a, b), temp
  nums = [i for i in range(a + 1, b)]
  print(b-a-1)
  print(*nums, end='')