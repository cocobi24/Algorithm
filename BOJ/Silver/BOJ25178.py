# https://www.acmicpc.net/problem/25178

n = int(input())
a, b = input().rstrip(), input().rstrip()
answer = [0] * 3

if sorted(a) == sorted(b):
  answer[0] = 1

if a[0] == b[0] and a[-1] == b[-1]:
  answer[1] = 1

for i in 'aeiou':
  a = a.replace(i, '')
  b = b.replace(i, '')

if a == b:
  answer[2] = 1

print('YES' if sum(answer) == 3 else "NO")