# https://www.acmicpc.net/problem/11328

n = int(input())
for _ in range(n):
  x, y = map(list, input().rstrip().split())

  if len(x) != len(y):
    print("Impossible")
  else:
    xx = [0] * 26
    yy = [0] * 26
    for i in range(len(x)):
      xx[ord(x[i]) - 97] += 1
      yy[ord(y[i]) - 97] += 1
    print("Possible" if xx == yy else "Impossible")