# https://www.acmicpc.net/problem/30501

n = int(input())
for _ in range(n):
  name = input().rstrip()
  if 'S' in name:
    print(name)
    break