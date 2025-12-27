# https://www.acmicpc.net/problem/9971

Cipher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Plain = ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U']

TRANS_SET = {}
for i in range(26):
  TRANS_SET[Cipher[i]] = Plain[i]

while True:
  start = input().rstrip()
  if start == 'ENDOFINPUT':
    break
  text = list(input().rstrip())
  end = input()

  ans = ''
  for t in text:
    ans += t if not t.isupper() else TRANS_SET[t]
  print(ans)