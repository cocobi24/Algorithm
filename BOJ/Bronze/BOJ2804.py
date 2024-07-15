# https://www.acmicpc.net/problem/2804

A, B = map(str, input().split())
len_A, len_B = len(A), len(B)

flag = 0
for i in range(len_A):
  for j in range(len_B):
    if A[i] == B[j]:
      col, row, flag = i, j, 1
      break
  if flag == 1 :
    break

for i in range(len_B):
  print(A if i == row else '.' * col + B[i] + '.' * (len_A - col - 1))