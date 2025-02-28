# https://www.acmicpc.net/problem/16428

A, B = map(int, input().split())
q, r = A // B, A % B
if B < 0:
  q = -(A//-B)
  r = A % -B
print(q)
print(r)