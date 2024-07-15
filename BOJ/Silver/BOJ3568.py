# https://www.acmicpc.net/problem/3568

s = input().rstrip().replace(',', '').replace(';', '').split()
TYPE = s[0]

for i in range(1, len(s)):
  name = ''
  t = ''
  for n in s[i]:
    if n.isalpha():
      name += n
    else:
      t += n
  t = t[::-1].replace('][', '[]')
  print(TYPE + t, name+';')