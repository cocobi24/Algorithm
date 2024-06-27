# https://www.acmicpc.net/problem/9455

T = int(input())

for _ in range(T):
  m, n = map(int, input().split())
  ans = 0

  box = []
  for _ in range(m):
    box.append(list(map(int, input().split())))

  for i in range(n):
    level, flag = 0, True
    for j in range(m):
      if box[j][i] == 1:
        flag = True
        level += 1
      if flag and box[j][i] == 0:
        ans += (1 * level)
  print(ans)