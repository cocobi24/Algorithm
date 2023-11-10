# https://www.acmicpc.net/problem/12755

n = int(input())
i = 0
while n > 0:
  i += 1
  s = str(i)
  n -= len(s)
  if n <= 0:
    answer = s[len(s) - 1 + n]
print(answer)