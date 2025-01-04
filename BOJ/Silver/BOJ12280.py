# https://www.acmicpc.net/problem/12280

import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T+1):
  N = int(input())
  book = list(map(int, input().split()))

  book_type, alex, bob = [], [], []
  for b in book:
    if b % 2 == 0:
      book_type.append(1)
      bob.append(b)
    else:
      book_type.append(0)
      alex.append(b)
  alex.sort(reverse=True)
  bob.sort()

  ans = []
  for _ in book_type:
    if _ == 0:
      ans.append(alex.pop())
    else:
      ans.append(bob.pop())
  print(f"Case #{i}:", *ans)
