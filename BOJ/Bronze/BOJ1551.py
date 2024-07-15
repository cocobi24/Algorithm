# https://www.acmicpc.net/problem/1551

N, K = map(int, input().split())
A = list(map(int, input().split(',')))
B = [0] * N

for _ in range(K):
  l = len(B) - 1
  for i in range(l):
    B[i] = A[i+1] - A[i]
  A = [*B]

print(*A[:N-K], sep=',')