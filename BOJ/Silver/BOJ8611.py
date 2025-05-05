# https://www.acmicpc.net/problem/8611

def to_base(n, k):
  result = []
  while n > 0:
    n, remainder = divmod(n, k)
    result.append(str(remainder))
  return ''.join(reversed(result))

n = int(input())
ans = []
for i in range(2, 11):
  a = to_base(n, i)
  if a == a[::-1]:
    ans.append(f'{i} {a}')
if len(ans) == 0:
  print("NIE")
else:
  print(*ans, sep='\n')
