# https://www.acmicpc.net/problem/1384

import sys
input = sys.stdin.readline
group_num = 1
while True:
  n = int(input())
  if n == 0:
    break

  group = []
  for i in range(n):
    name = list(map(str, input().rstrip().split()))
    group.append(name)

  nobody = True
  print(f"Group {group_num}")
  for i in range(n):
    for j in range(1, n):
      if group[i][j] == "N":
        target = i - j
        nasty = target if target >= 0 else n + target
        print(f"{group[nasty][0]} was nasty about {group[i][0]}")
        nobody = False

  if nobody:
    print("Nobody was nasty")
  print()
  group_num += 1