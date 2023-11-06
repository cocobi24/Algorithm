# https://www.acmicpc.net/problem/1783

n, m = map(int, input().split())
answer = m - 2
if n == 1:
  answer = 1
elif n == 2:
  answer = min(4, (m - 1) // 2 + 1)
elif m <= 6:
  answer = min(4, m)
print(answer)