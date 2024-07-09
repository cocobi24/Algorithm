# https://www.acmicpc.net/problem/2954

vowel = ['a', 'e', 'i', 'o', 'u']
remove = ['apa', 'epe', 'ipi', 'opo', 'upu']
s = input().rstrip()
for i in range(5):
  s = s.replace(remove[i], vowel[i])
print(s)