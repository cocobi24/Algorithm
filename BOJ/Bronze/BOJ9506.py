# https://www.acmicpc.net/problem/9506

import sys
sys.setrecursionlimit(10**7)

def getDiv(n, s, std):
  if n == 0:
    return s
  if std % n == 0:
    s.append(n)
  return getDiv(n - 1, s, std)

while True:
  n = int(input())
  if n == -1:
    break

  div = []
  divList = sorted(getDiv(n // 2, div, n))
  if sum(divList) == n:
    print(f"{n} = ", end='')
    print(*divList, sep=' + ')
  else:
    print(f"{n} is NOT perfect.")