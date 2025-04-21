# https://www.acmicpc.net/problem/6609

import sys
input = sys.stdin

while True:
  inp = input.readline().rstrip()
  if inp == "":
    break
  M, P, L, E, R, S, N = map(int, inp.split())

  for i in range(N):
    L_next = M * E
    P_next = L // R
    M_next = P // S
    L, P, M = L_next, P_next, M_next
  print(M)