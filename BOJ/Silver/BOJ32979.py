# https://www.acmicpc.net/problem/32979

from collections import deque

N = int(input())
T = int(input())
A = deque(list(map(int, input().split())))
B = list(map(int, input().split()))

ans = []
for b in B:
  A.rotate(-b + 1)
  ans.append(A[0])
print(*ans)