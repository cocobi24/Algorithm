# https://www.acmicpc.net/problem/29791

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

a_cnt, a_cool = 1, A[0] + 100
for i in range(1, N):
  if A[i] >= a_cool:
    a_cool = A[i] + 100
    a_cnt += 1

b_cnt, b_cool = 1, B[0] + 360
for i in range(1, M):
  if B[i] >= b_cool:
    b_cool = B[i] + 360
    b_cnt += 1

print(a_cnt, b_cnt)