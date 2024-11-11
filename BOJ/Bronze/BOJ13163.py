# https://www.acmicpc.net/problem/13163

n = int(input())
for _ in range(n):
  names = list(map(str, input().rstrip().split()))
  names[0] = 'god'
  print(''.join(names))