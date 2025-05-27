# https://www.acmicpc.net/problem/30045

n = int(input())

ans = 0
for _ in range(n):
  s = input().rstrip()
  if '01' in s or 'OI' in s:
    ans += 1
print(ans)