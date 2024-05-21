# https://www.acmicpc.net/problem/30664

while True:
  n = int(input())
  if n == 0:
    break
  print("TENTE NOVAMENTE" if n % 42 else "PREMIADO")