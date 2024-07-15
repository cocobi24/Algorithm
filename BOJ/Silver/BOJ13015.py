# https://www.acmicpc.net/problem/13015

temp = [0] + [i for i in range(1, 1000, 2)]

def print_star(i, n):
  if i == n:
    print('*' * n,' ' * temp[i-1], '*' * n, sep='')
  elif i == 1:
    print(' ' * (n-i), '*', ' ' * (n-2), '*', ' ' * (n-2), '*', sep='')
  else:
    print(' ' * (n-i), '*', ' ' * (n-2), '*', ' ' * temp[i-1], '*', ' ' * (n-2), '*', sep='')

n = int(input())
for i in range(n, 0, -1):
  print_star(i, n)
for i in range(2, n+1):
  print_star(i, n)