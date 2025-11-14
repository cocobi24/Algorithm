# https://www.acmicpc.net/problem/23810

N = int(input())

def printF(n, r, message):
  for _ in range(r):
    print(n * message)

printF(N, N, "@@@@@")
printF(N, N, "@")
printF(N, N, "@@@@@")
printF(N, N * 2, "@")