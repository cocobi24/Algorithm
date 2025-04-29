# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())
cnt = 0

for i in range(1, N):
  if N % i == 0:
    cnt += 1
    if cnt == K:
      print(i)
      exit()
cnt += 1
print(N if cnt == K else 0)