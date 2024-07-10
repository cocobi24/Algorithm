# https://www.acmicpc.net/problem/25709

n = list(input().rstrip())
cnt = 0
while True:
  if '1' in n:
    n.remove('1')
    cnt += 1
    if n == []:
      break
    n = list(str(int(''.join(n))))
  else:
    n = list(str(int(''.join(n)) - 1))
    cnt += 1
  if n == ['0']:
    break

print(cnt)