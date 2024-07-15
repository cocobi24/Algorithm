# https://www.acmicpc.net/problem/13022

target = input().rstrip()
for i in range(1, 13):
  wolf = 'w' * i + 'o' * i + 'l' * i + 'f' * i
  target = target.replace(wolf, '-')
target = target.replace('-', '')
print(1 if len(target) == 0 else 0)