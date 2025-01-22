# https://www.acmicpc.net/problem/1002

T = int(input())
for _ in range(T):
  n = input().rstrip()
  newN = 0
  cnt = 0
  while n != newN:
    if cnt != 0:
      n = newN
    num = list(map(int, sorted(n)))
    maxN =  num[0] + (num[1] * 10) + (num[2] * 100) + (num[3] * 1000)
    minN = (num[0] * 1000) + (num[1] * 100) + (num[2] * 10) + num[3]
    newN = str(maxN - minN)
    if len(newN) != 4:
      newN += "0"
    cnt += 1
  print(cnt - 1, newN, n)