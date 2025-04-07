# https://www.acmicpc.net/problem/33709

sep = ['.', '|', ':', '#']
n = int(input())
s = input().rstrip()
for _ in sep:
  s = s.replace(_, ' ')
s = map(int, s.split(' '))
print(sum(s))