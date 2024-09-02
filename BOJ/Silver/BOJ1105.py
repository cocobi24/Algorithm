# https://www.acmicpc.net/problem/1105

L, R = input().split()
l = len(L)
answer = 0
for i in range(l):
  if L[i] == R[i]:
    if L[i] == '8':
      answer += 1
  else:
    break
print(answer if len(L) == len(R) else 0)