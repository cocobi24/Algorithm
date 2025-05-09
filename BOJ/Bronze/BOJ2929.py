# https://www.acmicpc.net/problem/2929

code = input()
n = len(code)

cur, i, ans = 0, 0, 0
while i < n:
  if cur % 4 != 0:
    x = 4 - (cur % 4)
    ans += x
    cur += x

  cur += 1
  i += 1

  cnt = 0
  if i < n:
    j = i
    while j < n and 'a' <= code[j] <= 'z':
      cnt += 1
      j += 1
    cur += cnt
    i = j

print(ans)