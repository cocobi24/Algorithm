# https://www.acmicpc.net/problem/24051

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def insertion_sort(A, K):
  cnt = 0
  for i in range(1, N):
    loc = i - 1
    newItem = A[i]
    while 0 <= loc and newItem < A[loc]:
      A[loc + 1] = A[loc]
      cnt += 1
      if cnt == K:
        return A[loc]
      loc -= 1

    if loc + 1 != i:
      A[loc + 1] = newItem
      cnt += 1

    if cnt == K:
      return newItem
  return -1

print(insertion_sort(A, K))