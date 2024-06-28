# https://www.acmicpc.net/problem/9324

T = int(input())

for _ in range(T):
  M = list(input().rstrip())
  count_set = {chr(i):0 for i in range(65, 91)}
  ans = "OK"
  for i in range(len(M)):
    count_set[M[i]] += 1
    if count_set[M[i]] == 3:
      if i == len(M)-1:
        ans = "FAKE"
        break

      if M[i] == M[i+1]:
        count_set[M[i]] = -1
      else:
        ans = "FAKE"
        break
  print(ans)