# https://www.acmicpc.net/problem/20125

n = int(input())
cookies = [0] * 5
head, heart = 0, [0, 0]
for i in range(n):
  row = list(input().rstrip())
  if head == 0 and row.count('*') == 1:
    head = 9999
    heart = [i, row.index('*')]
  if i == heart[0] + 1:
    cookies[0] = row[:heart[1]].count('*')
    cookies[1] = row[heart[1] + 1:].count('*')
  elif i >= heart[0] + 2:
    cookies[2] += 1 if row[heart[1]] == '*' else 0
    cookies[3] += 1 if row[heart[1]-1] == '*' else 0
    cookies[4] += 1 if row[heart[1]+1] == '*' else 0
print(heart[0] + 2, heart[1] + 1, sep=' ')
print(*cookies)