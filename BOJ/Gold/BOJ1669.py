# https://www.acmicpc.net/problem/1669

X, Y = map(int, input().split())
ans = 0

if X != Y:
  n = int((Y - X)**0.5)
  m = (Y - X) - n**2
  if n**2 == Y - X:
    ans = 2 * n - 1
  else:
    ans = (2 * n) if m <= n else (2 * n + 1)
print(ans)