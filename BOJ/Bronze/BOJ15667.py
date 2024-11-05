# https://www.acmicpc.net/problem/15667

def getAnswer(n):
  for i in range(1, n + 1):
    if 1 + i + i ** 2 == n:
      break
  return i

ans = getAnswer(int(input()))
print(ans)