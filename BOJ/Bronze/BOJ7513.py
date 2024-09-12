# https://www.acmicpc.net/problem/7513

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  m = int(input())
  word = [input().rstrip() for _ in range(m)]
  n = int(input())
  password = [input().rstrip() for _ in range(n)]

  if i != 0:
    print()
  print(f"Scenario #{i + 1}:")

  for j in range(n):
    pwd = list(password[j].split(' '))[1::]
    ans = []
    for p in pwd:
      ans.append(word[int(p)])
    print(''.join(ans))