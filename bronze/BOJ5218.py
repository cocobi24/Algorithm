# https://www.acmicpc.net/problem/5218

alpha = {chr(i):i for i in range(65, 91)}
n = int(input())

for _ in range(n):
  X, Y = map(list, input().rstrip().split())
  answer = 'Distances:'
  for i in range(len(X)):
    x, y  = alpha[X[i]], alpha[Y[i]]
    d = y - x if y >= x else y - x + 26
    answer += ' ' + str(d)
  print(answer)