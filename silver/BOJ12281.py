# https://www.acmicpc.net/problem/12281

import sys
input = sys.stdin
input = list(input)
input.reverse()

T = int(input.pop().rstrip())
for i in range(T):
  n = int(input.pop().rstrip())
  books = list(map(int, input.pop().rstrip().split()))
  alex = sorted(filter(lambda x: x % 2 != 0, books))
  bob = sorted(filter(lambda x: x % 2 == 0, books), reverse=True)
  alex.reverse()
  bob.reverse()
  
  ans = []
  for j in range(n):
    ans.append(str(bob.pop()) if books[j] % 2 == 0 else str(alex.pop()))

  print(f"Case #{i+1}: {' '.join(ans)}")